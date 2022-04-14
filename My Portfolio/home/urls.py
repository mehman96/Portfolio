from django.urls import path
from .views import about,home

app_name="contact"

urlpatterns = [
    path('', home, name='home'),
    path('', about, name='about'), 
   
]
