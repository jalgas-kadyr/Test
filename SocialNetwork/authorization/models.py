from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    age = models.IntegerField()
    mail = models.CharField(max_length=50)
    friends = models.CharField(max_length=1000)
    notices = models.IntegerField()
