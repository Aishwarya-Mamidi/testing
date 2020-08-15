from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Adminl(models.Model):
    admin_id=models.CharField(max_length=25,primary_key=True)
    password=models.CharField(max_length=25)

class SignUp(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    uname=models.CharField(max_length=25,primary_key=True)
    psw=models.CharField(max_length=25)
    email=models.EmailField(max_length=254)
    def __str__(self):
        return self.uname
