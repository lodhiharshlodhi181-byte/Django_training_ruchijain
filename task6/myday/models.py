from django.db import models

# Create your models here.
class product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=40)
    pprice = models.IntegerField()
    poffer = models. FloatField()
    def __str__(self):
            return self.pname

