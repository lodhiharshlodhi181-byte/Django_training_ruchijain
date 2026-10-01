from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myday.models import product
from django.urls import reverse

# Create your views here.
def saveuser(request):    #create record ( C of CRUD)
    pid = 10
    pname = "masala dosa"
    pprice = 120
    poffer = 1

    pro = product(pid=pid,pname=pname,pprice=pprice,poffer=poffer)
    pro.save()
    url=reverse('index')
    return HttpResponseRedirect(url)
def index(request):
    indexs = product.objects.all()
    res=render(request,'index.html',{'indexs':indexs})
    return res


