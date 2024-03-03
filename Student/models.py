from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    studentname = models.CharField(max_length=100)
    studentemail = models.EmailField()
    studentvillage = models.CharField(max_length=100)
    studentpassword = models.CharField(max_length=100)
    studentbranch = models.CharField(max_length=100)
    studentphno = models.IntegerField()
    
    