from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email=models.CharField(max_length=15)
    phone=models.CharField(max_length=10)

class employee(models.Model):
    email=models.CharField(max_length=15)
    emp_id=models.IntegerField()
    company=models.CharField(max_length=15)
    desigination=models.CharField(max_length=15)
    place=models.CharField(max_length=15)
    salary=models.IntegerField()
