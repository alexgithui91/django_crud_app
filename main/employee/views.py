from django.shortcuts import render

# Create your views here.
def employees_list(request):
    return render(request, "employee/list.html", context)


def create_employee(request):
    return render(request, "employee/create.html", context)


def edit_employee(request):
    return render(request, "employee/edit.html", context)


def delete_employee(request):
    return render(request, "employee/delete.html", context)
