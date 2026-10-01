from django.urls import path
from CS import views

urlpatterns = [
    path("aboutcs/", views.aboutcs),
]