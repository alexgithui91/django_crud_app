from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employees_list(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees,
    }
    return render(request, "employee/list.html", context)


def create_employee(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    return render(request, "employee/create.html", context)


def edit_employee(request, pk):
    return render(request, "employee/edit.html", context)


def delete_employee(request, pk):
    return render(request, "employee/delete.html", context)
