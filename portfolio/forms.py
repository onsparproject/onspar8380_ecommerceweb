from django import forms
from .models import Employee


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'address', 'emp_number', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


