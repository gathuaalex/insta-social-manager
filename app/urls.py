from django.urls import path
from .views import Home,PersonCreateView,Dashboard

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('', PersonCreateView.as_view(), name='null'), # new
    path('dash/',Dashboard.as_view(),name='dashdash')
]
