from django.urls import path
from .views import Home,PersonCreateView

urlpatterns = [
    path('', PersonCreateView.as_view(), name='home'), # new
]
