
from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages



def feedback(request):

    if request.method=="POST":       
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Feedback(name=name, email=email, message=message)
        contact.save()
        alert = True
        return render(request, 'contact.html', {'alert':alert})
    return render(request, "contact.html")

