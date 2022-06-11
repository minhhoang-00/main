from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(default=0)