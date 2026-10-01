from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from placementprediction.models import student
from django.urls import reverse
from django.template import loader
import joblib 
# Create your views here.
def home(request):
    return render(request,'home.html')
def registraion(request):
    return render(request,'studentreg.html')
def saveuser(request):
    if request.method == "POST":
        sname = request.POST['sname']
        spassword = request.POST['spassword']
        sid = request.POST['sid']
        sbranch = request.POST['sbranch']
        semail = request.POST['semail']

        user1 = student(
            sname=sname,
            spassword=spassword,
            sid=sid,
            sbranch=sbranch,
            semail=semail
        )

        user1.save()
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'studentreg.html',
                      {
                          'errormsg':'username Already exists'
                      })
def login(request):
    return render(request,'login.html')

def loginvalidation(request):
    try:
        user1=studentreg.objects.get(
            sname=request.POST['sname'],
            spassword=request.POST['spassword']
           
        )
        return HttpResponseRedirect(reverse('home'))
    except studentreg.DoesNotExist:
        return render(request,'login.html',{'erg':'invalid username or password'})
    
def splacement(request):
    return render(request,'splacement.html')
def result(request):
    scaler=joblib.load('scalermodel (1).pkl')
    mlmodel=joblib.load('mlmodel (1).pkl')
    lis=[]
    lis.append(request.GET['IQ'])
    lis.append(request.GET['CGPA'])
    lis.append(request.GET['PROFILE'])
    scaled_input=scaler.transform([lis])
    ans=mlmodel.predict(scaled_input)[0]
    # 0 or 1 ko message me convert karna
    if ans == 1:
        result_message = "Congratulations! Student ko placement milegi."
    else:
        result_message = "Sorry! Student ko placement nahi milegi."

    res = render(
        request,
        'result.html',
        {
            'ans': ans,
            'lis': lis,
            'result_message': result_message
        }
    )

    return res
def studentreg(request):
    return render(request,'studentreg.html')
    