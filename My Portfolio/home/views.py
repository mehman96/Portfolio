from django.shortcuts import render
from .models import Testimonial,Blog

def home(request):
  teams=Testimonial.objects.all()
  items=Blog.objects.all()
  context = {
        'teams': teams,
        'items': items
    }
  return render(request, 'index.html',context)


def about (request):
   return render(request, 'about.html')