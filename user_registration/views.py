from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.

def registration(response):
  if response.method == "POST":
    form = RegistrationForm(response.POST)
    if form.is_valid():
      form.save()
    return redirect("/")
  else:    
    form = RegistrationForm()
    return render(response, "registration.html", {"form": form}) 
