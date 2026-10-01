from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    s="<H1>INFORMATION ABOUT SISTEC</H1>"
    s="<h1>principal : Dr. Manish Billore</h1>"
    s="<h1>address : Opposite bhopal airport</h1>"
    return HttpResponse(s)  
