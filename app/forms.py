from allauth.account.forms import SignupForm
from django import forms 
from django.contrib.auth.models import User 
from .models import *

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


class ModifiedSignup(SignupForm):
    def __init__(self, *args, **kwargs):
        super(ModifiedSignup,self).__init__(*args, **kwargs)
        
      #  self.fields['firstname']=forms.CharField(max_length=10,label='Firstname',required=True)   
    #def save(self, request):
        #firstname=self.cleaned_data.pop('firstname')
       # return super(ModifiedSignup,self).save(request)    




