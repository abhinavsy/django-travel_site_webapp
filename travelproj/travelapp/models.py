from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Team(models.Model):
    img=models.ImageField(upload_to='pictures')
    name=models.CharField(max_length=200)
    desc=models.TextField(default='SOME STRING')
