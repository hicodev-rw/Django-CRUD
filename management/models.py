from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=60)
    occupation = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, default=0)
    gender = models.CharField(max_length=1)
