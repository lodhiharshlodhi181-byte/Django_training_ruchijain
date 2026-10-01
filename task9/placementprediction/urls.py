from django.urls import path
from .views import *
urlpatterns = [
    path("splacement/", splacement, name="splacement"),
    path("saveuser/", saveuser, name="saveuser"),
    path("login/", login, name="login"),
    path("loginvalidation/", loginvalidation, name="loginvalidation"),
    path("home/", home, name="home"),
    path("result/",result, name="result"),
    path("registraion/", registraion, name="registraion"),
    path("studentreg/", studentreg, name="studentreg"),

]