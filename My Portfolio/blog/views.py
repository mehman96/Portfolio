from django.shortcuts import render
from django.views.generic import  ListView
from home.models import Blog







class BlogListView(ListView):
    model = Blog
    paginate_by = 3
    template_name = 'blog.html'
    context_object_name='items'
