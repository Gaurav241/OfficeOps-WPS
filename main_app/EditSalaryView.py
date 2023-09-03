from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from .models import Department, Manager, Employee, EmployeeSalary
from .forms import EditSalaryForm
from django.urls import reverse


class EditSalaryView(View):
    def get(self, request, *args, **kwargs):
        salaryForm = EditSalaryForm()
        manager = get_object_or_404(Manager, admin=request.user)
        salaryForm.fields['department'].queryset = Department.objects.filter(division=manager.division)
        context = {
            'form': salaryForm,
            'page_title': "Edit Employee's Salary"
        }
        return render(request, "manager_template/edit_employee_salary.html", context)

    def post(self, request, *args, **kwargs):
        form = EditSalaryForm(request.POST)
        context = {'form': form, 'page_title': "Edit Employee's Salary"}
        if form.is_valid():
            try:
                employee = form.cleaned_data.get('employee')
                department = form.cleaned_data.get('department')
                base = form.cleaned_data.get('base')
                ctc = form.cleaned_data.get('ctc')
                # Validating
                salary = EmployeeSalary.objects.get(employee=employee, department=department)
                salary.ctc = ctc
                salary.base = base
                salary.save()
                messages.success(request, "Salary Updated")
                return redirect(reverse('edit_employee_salary'))
            except Exception as e:
                messages.warning(request, "Salary Could Not Be Updated")
        else:
            messages.warning(request, "Salary Could Not Be Updated")
        return render(request, "manager_template/edit_employee_salary.html", context)
