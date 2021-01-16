from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'courses/signup.html', context=context)

def login_view(request):
    return render(request, 'courses/login.html')

def logout_view(request):
    return render(request, 'courses/logout.html')