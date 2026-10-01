from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def harsh(request):
    s="<h1>hello harsh</h1>"
    return HttpResponse(s)
def dept(request):
    s="""
<p>Department of Computer Science and Engineering</p>
HOD: Dr Vasima Khan
ADDRESS: 3rd floor main building
</p>
"""
    return HttpResponse(s)
