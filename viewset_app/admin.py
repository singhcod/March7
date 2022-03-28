from django.contrib import admin

# Register your models here.
from viewset_app.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['ename','department','esalary']