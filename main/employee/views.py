from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def employees_list(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees,
    }
    return render(request, "employee/list.html", context)


def create_employee(request):
    return render(request, "employee/create.html", context)


def edit_employee(request, pk):
    return render(request, "employee/edit.html", context)


def delete_employee(request, pk):
    return render(request, "employee/delete.html", context)
