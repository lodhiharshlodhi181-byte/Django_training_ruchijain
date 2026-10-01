from django.urls import path
from . views import *
urlpatterns=[
     path('saveuser/',saveuser, name='saveuser'),
     path('inedx/',index,name='index'),
 ]