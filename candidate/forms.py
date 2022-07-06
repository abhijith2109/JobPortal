from django import forms
from candidate.models import CandidateProfile


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model=CandidateProfile
        exclude=("user",)

        widgets = {
            "profile_pic": forms.FileInput(attrs={"class": "form-control", "placeholder": "Add Profile Picture"}),
            "qualification": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Qualification*"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Age"}),
            "skills": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Skills*"}),
            "cv": forms.FileInput(attrs={"class": "form-control", "placeholder": "Add Your Resume"}),

        }