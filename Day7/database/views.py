from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from database.models import Employee
from django.urls import reverse


# Create your views here.
def newEmployeeForm(request):
    res=render(request,'newEmployeeForm.html')
    return res

def saveuser(request):    #create record ( C of CRUD)
    Eno = request.POST['Eno']
    ename = request.POST['ename']
    esal = request.POST['esal']
    emp = Employee(Eno=Eno,ename=ename,esal=esal)
    emp.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)
def employeelist(request):           #read records (R of CRUD)
    Employees= Employee.objects.all()          # it return querry set of employee objectres
    res= render(request,'employeelist.html',{'Employees':Employees})
    return res

def updateEmployeeForm(request):
    id=request.GET['id']
    employee=Employee.objects.filter(id=id).values()
    res=render(request,'updateEmployeeForm.html',{'employee':employee[0]})
    return res


def updateEmployee(request):
    id = request.POST['id']
    Eno = request.POST['Eno']
    ename = request.POST['ename']
    esal = request.POST['esal']
    Employee(id=id,Eno=Eno, ename=ename,esal=esal).save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)
def deleteEmployee(request):
    id=request.GET['id']
    emp=Employee.objects.filter(id=id)
    emp.delete()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)
def home(request):
    Employees = Employee.objects.all()
    return render(request, "employeelist.html", {"Employees": Employees})




    

