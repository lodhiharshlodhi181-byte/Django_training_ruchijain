from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutcs(request):
    s="<h1>this is CS department</h1>" 
    h="<h1>HOD: Dr. nargis gupta</h1>"
    f="<h1>faculties: Amit sir, Anshul sir, Arihant sir</h1>"
    return HttpResponse(s+h+f)
