from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('dash/', Dashboard.as_view(), name='dashdash')
]
