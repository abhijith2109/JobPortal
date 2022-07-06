from django import forms
from employer.models import EmployerProfile, Jobs
from ckeditor.fields import CKEditorWidget


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ("user",)

        widgets = {
            "company_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Company Name *"}),
            "address": forms.Textarea(attrs={"class": "form-control", "placeholder": "Company Address","style":"height: 142px;"}),
            "company_website": forms.URLInput(attrs={"class": "form-control", "placeholder": "Website link/Email link*"}),
            "about_us": forms.Textarea(attrs={"class": "form-control", "placeholder": "About us*","style":"height: 200px;"}),
            "services": forms.Select(attrs={"class": "form-select","placeholder":"Select services"}),

        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude = ("posted_by", "created_date")



        widgets={
            "job_title": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Job Tilte"}),
            "job_description": forms.Textarea(attrs={"class":"form-control","placeholder":"Enter Job description,responsibilties,etc"}),
            "experiance": forms.NumberInput(attrs={"class":"form-control","placeholder":"Experiance, default value will be 0"}),
            "location": forms.TextInput(attrs={"class": "form-control","placeholder":"Enter Location"}),
            "salary": forms.NumberInput(attrs={"class":"form-control","placeholder":"Salary(optional)"}),
            "last_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "qualification": forms.TextInput(attrs={"class":"form-control","placeholder":"Qualification for job (optional)"})
        }