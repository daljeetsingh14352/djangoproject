from django.db import models

# Create your models here.
class empeemastertable(models.Model):
    Code=models.IntegerField()
    Name=models.CharField(max_length=100)
    DOJ=models.DateField()
    Gender=models.CharField(max_length=1)
    State=models.CharField(max_length=100)
    CTC=models.IntegerField()

class salarydetails(models.Model):
    Code=models.IntegerField()  