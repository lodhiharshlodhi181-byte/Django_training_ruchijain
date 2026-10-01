from django.contrib import admin
from django.urls import path
from jinja import views

urlpatterns = [
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("result/",views.result),
    path("info/",views.info),
    path("testpaper/",views.testpaper),
    path("sum/",views.sum),
    path("admin/", admin.site.urls),
]