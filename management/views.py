from django.http import HttpResponseRedirect
from django.shortcuts import render
from management.models import Employee


def show_emp(request):
    show_all = Employee.objects.all()
    return render(request, 'index.html', {"data": show_all})


def new_emp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    occupation = request.POST.get('occupation')
    gender = request.POST.get('gender')
    salary = request.POST.get('salary')
    if request.method == 'POST':
        if name and email and occupation and salary and gender:
            save_record = Employee()
            show_data = Employee.objects.all()
            save_record.name = name
            save_record.email = email
            save_record.occupation = occupation
            save_record.salary = request.POST.get('salary')
            save_record.gender = gender
            save_record.save()
            show_data = Employee.objects.all()
            info = name
            return HttpResponseRedirect("/")
            return render(request, 'index.html', {'data': show_data})
    else:
        return render(request, 'new_emp.html')


def update_emp(request, id):
    empobject = Employee.objects.get(id=id)
    return render(request, 'update_emp.html', {'Employee':empobject})


def updates(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    occupation = request.POST.get('occupation')
    gender = request.POST.get('gender')
    salary = request.POST.get('salary')
    if request.method == 'POST':
        save_record = Employee.objects.get(id=id)
        save_record.name = name
        save_record.email = email
        save_record.occupation = occupation
        save_record.salary = salary
        save_record.gender = gender
        if name and email and occupation and salary and gender:
            save_record.save()
            show_data=Employee.objects.all()
        return HttpResponseRedirect("/")
        return render(request, 'index.html', {'data': show_data})
    else:
        return render(request, 'update_emp.html',{'Employee':Employee.objects.get(id=id)})


def deletemp(request, id):
    delemployee = Employee.objects.get(id=id)
    delemployee.delete()
    show_data = Employee.objects.all()
    return HttpResponseRedirect("/")
    return render(request, 'index.html', {'data': show_data})


