from django.db import models

# Create your models here.



class MaxTemp(models.Model): # COMM0N
    year = models.CharField(max_length=100)
    data = models.JSONField(null=True, blank=True)
    city = models.CharField(max_length=200)