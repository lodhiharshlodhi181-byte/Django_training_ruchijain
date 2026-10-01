from django.urls import path
from .views import *
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("saveuser/", saveuser, name="saveuser"),
    path("saveuser1/", saveuser1, name="saveuser1"),
    path("login/", login, name="login"),
    path("loginvalidation/", loginvalidation, name="loginvalidation"),
    path("home/", home, name="home"),
    path("studentreg/",studentreg, name="studentreg"),
    path("final/", final, name="final"),
]