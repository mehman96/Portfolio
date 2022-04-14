from django.shortcuts import render
from .models import Portfolio
from django.views.generic import ListView


class portfolioListView(ListView):
    model = Portfolio
    paginate_by =2
    template_name = 'portfolio.html'
    context_object_name='projects'