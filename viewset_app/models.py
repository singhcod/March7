from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    esalary = models.IntegerField()


    def __str__(self):
        return self.ename