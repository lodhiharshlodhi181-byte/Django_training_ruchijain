from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutaids(request):
    s="<h1>this is AIDS department</h1>" 
    h="<h1>HOD: Dr. Vasima Khan</h1>"
    f="<h1>faculties: Ruchi mam, Sachin sir, Abhuday sir, Arihant sir</h1>"
    return HttpResponse(s+h+f)
