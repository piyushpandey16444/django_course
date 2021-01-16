from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError


class AuthenticationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password1"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        get_existing_user = User.objects.filter(email=email)
        if get_existing_user:
            raise ValidationError("User Exist")
        return email
