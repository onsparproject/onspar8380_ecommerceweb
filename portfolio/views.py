from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
#from shop.models import Product


@login_required
def home(request):
    return render(request,
                  'portfolio/home.html',
                  {'section': 'home'})

# User Login Methods SAVE!!!
'''
def notifications(request):
    products = Product.objects.all()
    requireRestock = []
    for product in products:
        if (product.stock <= 20):
            requireRestock.append(product)
    return render(request,'portfolio/notifications.html',{'notifications': requireRestock})
'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'portfolio/login.html', {'form': form})


# Employee CRUD Methods

@login_required
def employee_list(request):
    employees = Employee.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/employee_list.html', {'employees': employees})


@login_required
def employee_new(request):
   if request.method == "POST":
       form = EmployeeForm(request.POST)
       if form.is_valid():
           employee = form.save(commit=False)
           employee.created_date = timezone.now()
           employee.save()
           employees = Employee.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/employee_list.html',
                         {'employees': employees})
   else:
       form = EmployeeForm()
       # print("Else")
   return render(request, 'portfolio/employee_new.html', {'form': form})


@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
       # update
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.updated_date = timezone.now()
            employee.save()
            employees = Client.objects.filter(created_date__lte=timezone.now())
            return render(request, 'portfolio/employee_list.html',
                         {'employees': employees})
    else:
               # edit
            form = EmployeeForm(instance=employee)
            return render(request, 'portfolio/employee_edit.html', {'form': form})


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    employees = Employee.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/employee_list.html', {'employees': employees})


@login_required
def account_settings_list(request):
    return render(request,
                  'portfolio/account_settings_list.html',
                  {'section': 'account_settings_list'})

@login_required
def password_change_form(request):
    return render(request,
                  'registration/password_change_form.html',
                  {'section': 'password_change_form'})

@login_required
def password_change_done(request):
    return render(request,
                  'registration/password_change_done.html',
                  {'section': 'password_change_done'})


