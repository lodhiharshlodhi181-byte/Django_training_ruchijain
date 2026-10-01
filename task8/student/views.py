from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from student.models import user,student
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')
def saveuser(request):
    user1= user()
    u=user.objects.filter(username=request.POST['username'])
    if not u:
        user1.username=request.POST['username']
        user1.password=request.POST['password']
        user1.name=request.POST['name']
        user1.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'signup.html',
                      {
                          'errormsg':'username Already exists'
                      })
def saveuser1(request):
    user1= student()
    u=student.objects.filter(studentname=request.POST['studentname'])
    if not u:
        user1.studentid=request.POST['studentid']
        user1.studentname=request.POST['studentname']
        user1.studentbranch=request.POST['studentbranch']
        user1.save()
        return HttpResponseRedirect(reverse('final'))
    else:
        return render(request,'studentreg.html',
                      {
                          'errormsg':'username Already exists'
                      })
    

def login(request):
    return render(request,'login.html')

def loginvalidation(request):
    try:
        user1=user.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
           
        )
        return HttpResponseRedirect(reverse('home'))
    except user.DoesNotExist:
        return render(request,'login.html',{'erg':'invalid username or password'})

def studentreg(request):
    return render(request,'studentreg.html')
def final(request):
    return render(request,'final.html')


 