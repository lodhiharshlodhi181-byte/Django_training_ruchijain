from django.urls import path
from . import views

urlpatterns=[
    path('newEmployeeForm/',views.newEmployeeForm, name='newEmployeeForm'),
    path('deleteEmployee/',views.deleteEmployee,name="deleteEmployee"),
    path('updateEmployee/',views.updateEmployee, name="updateEmployee"),
    path('employeelist/',views.employeelist,name="employeelist"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path('updateEmployeeForm/',views.updateEmployeeForm, name='updateEmployeeForm')
    #path("", views.home, name="home"),

 ]