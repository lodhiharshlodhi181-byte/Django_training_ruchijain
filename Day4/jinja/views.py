from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que="who devlop python"
    a="harsh"
    b="dennis"
    c="Guide ven rossum"
    d=" harsh palet"
    context={'que':que,'a':a,'b':b,'c':c,d:'d'}
    template=loader.get_template("testpaper.html")
    res=template.render(context,request)
    return HttpResponse(res)
def info(request):
    Name="Name=Deepanshu Mehra"
    department="Department=CSE-AIDS"
    age="Age=21"

    context={
        'Name':Name,
        'department':department,
        'age':age

}
    template=loader.get_template('info.html')
    res=template.render(context,request)
    return HttpResponse(res)

def sum(request):
    a=10
    b=20
    c=30
    sum=a+b+c
    context={'a':a,'b':b,'c':c,'d':sum}
    template=loader.get_template('sum.html')
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    context={
        'name': "harsh lodhi",
        'marks': 90,
        
    }
    return render(request, 'result.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')