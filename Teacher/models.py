from django.db import models

# Create your models heTec
class TecDetailes(models.Model):
    Tecname = models.CharField(max_length=100)
    Tecpassword = models.CharField(max_length=100)
    Tecemail = models.EmailField()    
    Tecqulfication = models.CharField(max_length=100)
    TecExperence = models.IntegerField()
    Tecjoining = models.DateTimeField()
    Tecvillage = models.CharField(max_length=100)    
    Tecphoto = models.ImageField(upload_to='media/')
    