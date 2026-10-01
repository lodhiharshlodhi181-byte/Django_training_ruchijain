from django.db import models

# Create your models here.
class client(models.Model):
    clientid = models.IntegerField()
    clientname = models.CharField(max_length=30)
    clientcompany = models.CharField(max_length=30)
    def __str__(self):
        return self.clientname
class customer(models.Model):
    customerid = models.IntegerField()
    customername = models.CharField(max_length=30)
    customerphone = models.IntegerField()
    def __str__(self):
        return self.customername

class order(models.Model):
    orderid = models.IntegerField()
    ordername = models.CharField(max_length=30)
    orderprice = models.IntegerField()
    def __str__(self):
        return self.ordername