from django.db import models

# Create your models here.
class user(models.Model):
    username= models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.username
class student(models.Model):
    studentid=models.IntegerField(primary_key=True)
    studentname=models.CharField(max_length=20)
    studentbranch=models.CharField(max_length=20)
    def __str__(self):
        return self.studentname


