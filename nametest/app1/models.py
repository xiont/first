from __future__ import unicode_literals

from django.db import models
from MySQLdb.constants.ER import PRIMARY_CANT_HAVE_NULL

# Create your models here.
class Test(models.Model):
    username = models.CharField(max_length=32)
    studentnum = models.CharField(max_length=32)
    studentmajor = models.CharField(max_length=32)
    
class Login(models.Model):
    username = models.CharField(max_length=32)
    password1= models.CharField(max_length=32)
    password2 = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    idnumber = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    home = models.CharField(max_length=32)

    def __unicode__(self):
        return self.username