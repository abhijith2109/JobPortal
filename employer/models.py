from django.db import models
from users.models import User

# Create your models here.

class EmployerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="employers")
    company_name=models.CharField(max_length=120)
    bio=models.CharField(max_length=120)
    logo=models.ImageField(upload_to="images")
    location=models.CharField(max_length=60)
    services=models.CharField(max_length=130)
