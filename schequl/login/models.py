from django.db import models


# Create your models here.
class UserInfo(models.Model):
    fnm = models.CharField(max_length=20)
    lnm = models.CharField(max_length=20)
    birth = models.CharField(max_length=10)
    gen = models.CharField(max_length=10)
    marital = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
