from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    tokens = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=31)
    email = models.EmailField()
    address = models.CharField(max_length=200)