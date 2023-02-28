from django.db import models

# Create your models here.
class Todo(models.Model):
    make= models.CharField(max_length=100,default='default_value')
    model= models.CharField(max_length=100,default='default_value')
    year = models.CharField(max_length=100,default='default_value')
    color= models.CharField(max_length=100,default='default_value')
    price = models.CharField(max_length=500,default='default_value')
