from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField( max_length=50)
    mail=models.EmailField(max_length=30)