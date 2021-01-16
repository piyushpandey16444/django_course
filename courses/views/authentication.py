from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from courses.forms.authentication_form import AuthenticationForm


def signup_view(request):
    form = AuthenticationForm()
    context = {
        'form': form
    }
    if request.method == "GET":
        return render(request, 'courses/signup.html', context=context)
    else:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'courses/signup.html', context=context)


def login_view(request):
    return render(request, 'courses/login.html')


def logout_view(request):
    return render(request, 'courses/logout.html')
