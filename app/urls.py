from django.urls import path
from .views import Home, PersonCreateView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('', PersonCreateView.as_view(), name='null'),  # new
]
