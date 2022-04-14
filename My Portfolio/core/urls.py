
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls",namespace="home"),),
    path('about/',include("home.urls",namespace="about"),),
    path('blog/',include("blog.urls",namespace="blog"),),
    path('portfolio/',include("portfolio.urls",namespace="portfolio"),),
    path('contact/', include('contact.urls', namespace="feedback")),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
