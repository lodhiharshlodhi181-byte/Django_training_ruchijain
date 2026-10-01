from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from myuser.models import user
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
    


def login(request):
    return render(request,'login.html')

def loginvalidation(request):
    try:

        3333
        user1=user.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
           
        )
        #--------------------session create
        request.session['username']=user1.username
        request.session['name']=user1.name
        return HttpResponseRedirect(reverse('home'))
    except user.DoesNotExist:
        return render(request,'login.html',{'erg':'invalid username or password'})

def logout(request):     #delete session
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))
