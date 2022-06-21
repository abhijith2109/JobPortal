from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone=models.CharField(max_length=12)

    options=(
        ("EMPLOYER","EMPLOYER"),
        ("CANDIDATE","CANDIDATE")
    )
    role=models.CharField(max_length=12,choices=options,default="CANDIDATE")

    state_choices = (
    ("ANDHRA PRADESH", "ANDHRA PRADESH"), ("ARUNACHAL PRADESH ", "ARUNACHAL PRADESH "), ("ASSAM", "ASSAM"),
    ("BIHAR", "BIHAR"), ("CHHATTISGARH", "CHHATTISGARH"), ("GOA", "GOA"), ("GUJARAT", "GUJARAT"),
    ("HARYANA", "HARYANA"), ("HIMACHAL PRADESH", "HIMACHAL PRADESH"), ("JAMMU AND KASHMIR ", "JAMMU AND KASHMIR "),
    ("JHARKHAND", "JHARKHAND"), ("KARNATAKA", "KARNATAKA"), ("KERALA", "KERALA"), ("MADHYA PRADESH", "MADHYA PRADESH"),
    ("MAHARASHTRA", "MAHARASHTRA"), ("MANIPUR", "MANIPUR"), ("MEGHALAYA", "MEGHALAYA"), ("MIZORAM", "MIZORAM"),
    ("NAGALAND", "NAGALAND"), ("ODISHA", "ODISHA"), ("PUNJAB", "PUNJAB"), ("RAJASTHAN", "RAJASTHAN"),
    ("SIKKIM", "SIKKIM"), ("TAMIL NADU", "TAMIL NADU"), ("TELANGANA", "TELANGANA"), ("TRIPURA", "TRIPURA"),
    ("UTTAR PRADESH", "UTTAR PRADESH"), ("UTTARAKHAND", "UTTARAKHAND"), ("WEST BENGAL", "WEST BENGAL"),
    ("ANDAMAN AND NICOBAR ISLANDS", "ANDAMAN AND NICOBAR ISLANDS"), ("CHANDIGARH", "CHANDIGARH"),
    ("DADRA AND NAGAR HAVELI", "DADRA AND NAGAR HAVELI"), ("DAMAN AND DIU", "DAMAN AND DIU"),
    ("LAKSHADWEEP", "LAKSHADWEEP"), ("NATIONAL CAPITAL TERRITORY OF DELHI", "NATIONAL CAPITAL TERRITORY OF DELHI"),
    ("PUDUCHERRY", "PUDUCHERRY"))
    state = models.CharField(choices=state_choices, max_length=35,default="KERALA")

    @property
    def is_candidate(self):
        return self.role=="CANDIDATE"
    @property
    def is_employer(self):
        return self.role=="EMPLOYER"

