from django import forms

from django.contrib.auth.forms import UserCreationForm
from users.models import User
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Must have at least 6 characters*"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"ConfirmPassword*"}))

    class Meta:
        model=User
        fields=["username",
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
                "phone",
                "state",
                "role"]
        widgets={
            "username": forms.TextInput(attrs={"class": "form-control","placeholder":"Create UserName *"}),
            "first_name": forms.TextInput(attrs={"class": "form-control","placeholder":"What is your name? *"}),
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder":"Tell us your Email ID *"}),
            "phone": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter MobileNumber *"}),
            "state": forms.Select(attrs={"class": "form-select","placeholder":"Select State "}),
            "role": forms.Select(attrs={"class":"form-select"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"UserName"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

