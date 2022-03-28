import imp
from django.contrib import admin
from .models import student,Employee

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display=['name','roll','department']
class AdminEmployee(admin.ModelAdmin):
    list_display=['name','salery','JobType','joblocation']




admin.site.register(student,AdminStudent),
admin.site.register(Employee,AdminEmployee)
