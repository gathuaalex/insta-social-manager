from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfiles(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
   # This line is required.  Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.CASCADE)
# The additional attributes we wish to include.
    website = models.URLField(blank=True) 
    picture = models.ImageField(upload_to='profile_images', blank=True)
# Override the __unicode__() method to return out something meaningful!
    def __str__(self): 
         return self.email



class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self): 
        return self.email