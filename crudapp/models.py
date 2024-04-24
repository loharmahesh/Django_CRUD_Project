from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.FloatField()
    position = models.CharField(max_length=30)
    blood_g = models.CharField(max_length=50)
    age = models.IntegerField()