from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    department=models.CharField(max_length=1000)
