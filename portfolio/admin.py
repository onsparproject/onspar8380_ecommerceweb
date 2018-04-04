from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeList(admin.ModelAdmin):
    list_display = ('emp_number','name', 'address', 'city', 'state')
    list_filter = ('emp_number','name', 'address')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']

admin.site.register(Employee, EmployeeList)