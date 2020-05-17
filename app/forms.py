
from django import forms 
from django.contrib.auth.models import User 
from .models import Person

#inherits from class forms
class UserForm(forms.ModelForm): 
    #passwordinput() widget is used for hidding the password
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User #its must to supply the model field
        fields = ('username', 'email', 'password')#this shows the fields that should be present in the rendered form
class UserProfileForm(forms.ModelForm): 
     class Meta: 
         model = Person
         fields = ('name', 'email' ,'job_title','bio')


