from django.db import models

# Create your models here.
class student(models.Model):
    sid= models.IntegerField(primary_key=True)
    spassword=models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    sbranch=models.CharField(max_length=20)
    semail=models.CharField(max_length=30)

    def __str__(self):
        return self.sname