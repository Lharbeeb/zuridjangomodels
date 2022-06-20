from django.db import models

# Create your models here.


class post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField() 
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField

