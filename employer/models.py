from django.db import models
from users.models import User

# Create your models here.

class EmployerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employers")
    company_name=models.CharField(max_length=120)
    about_us=models.TextField(null=True)
    logo=models.ImageField(upload_to="images")
    address=models.TextField(max_length=260)
    company_website=models.URLField(max_length=120)
    services_choices = (
        ("Advertising", "Advertising"),
        ("ELectronics","ELectronics"),
        ("Financial Sevices", "Financial Sevices"),
        ("Market Reserarch", "Market Reserarch"),
        ("Govt.Sectors", "Govt.Sectors"),
        ("IT And Solutions", "IT And Solutions"),
        ("Media & Entertainment","Media & Entertainment"),
        ("Telecom Service","Telecom Service"),
        ("Others","Others")
    )
    services=models.CharField(max_length=130,choices=services_choices,default="Advertising")


class Jobs(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=120)
    job_description=models.TextField()
    experiance=models.PositiveIntegerField(default=0)
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    created_date=models.DateField(auto_now_add=True)
    last_date=models.DateField(null=True,blank=True)
    qualification=models.CharField(max_length=120,null=True,blank=True)


    def __str__(self):
        return self.job_title

class Applications(models.Model):
     applicant=models.ForeignKey(User,on_delete=models.CASCADE,related_name="applicant")
     job=models.ForeignKey(Jobs,on_delete=models.CASCADE,related_name="ajob")
     options=(
         ("applied","applied"),
         ("rejected","rejected"),
         ("cancelled","cancelled"),
         ("accepted","accepted")
     )
     status=models.CharField(max_length=120,choices=options,default="applied")
     date=models.DateField(auto_now_add=True)

     class Meta:
         unique_together=(
             "applicant","job"
         )
         # unique_together -restrict multiple record of same pair
         #ie one applicant -one job -one time add,

