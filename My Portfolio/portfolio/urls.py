from django.urls import path
from .views import portfolioListView

app_name="portfolio"

urlpatterns = [
    path('', portfolioListView.as_view(), name='portfolio'),
   
]
