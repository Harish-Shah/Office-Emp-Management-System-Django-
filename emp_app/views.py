from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from django.db.models import Q
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp=Employee(first_name=first_name, last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('An Exception occured! Employee not added')

def remove_emp(request,emp_id= 0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee removed Succesfully')
        except:
            return HttpResponse('Please Choose a Valid Emp Id')

    emps= Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
    #i help to avoid case sensitive letters i.e haris and Haris will be same
    #contains is used to boost the boost the search i.e. it will search Haris if we enter only 'ar' as well
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
