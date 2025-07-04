from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from employees.decorators import employee_login_required

@employee_login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})
@employee_login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html', {'form': form})

@employee_login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html', {'form': form})

@employee_login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})