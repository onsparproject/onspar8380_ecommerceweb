from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Employee(models.Model):
    emp_number = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=200)
    cell_phone = models.IntegerField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.emp_number)