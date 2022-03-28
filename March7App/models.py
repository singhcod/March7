from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    department=models.CharField(max_length=1000)
class Employee(models.Model):
    name=models.ForeignKey(student, on_delete=models.CASCADE)
    salery=models.IntegerField()
    JobType=models.CharField(max_length=100)
    joblocation=models.CharField(max_length=100)
