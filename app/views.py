from django.shortcuts import render
from .forms import UserProfileForm
from .models import Person
# Create your views here.
# config/views.py
from django.views.generic import TemplateView,CreateView



class Home(TemplateView):
    template_name = 'person_form.html'
    

class PersonCreateView(CreateView):
    
    form_class=UserProfileForm
    template_name = 'person_form.html'
    