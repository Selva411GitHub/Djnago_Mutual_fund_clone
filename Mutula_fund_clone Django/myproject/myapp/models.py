from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    fund_house = models.CharField(max_length=255)
    fund_number = models.CharField(max_length=10)  # Adjust the max_length as needed
    unit_held = models.FloatField()
    invested = models.FloatField()
    currentvalue = models.FloatField(default=0.0) 
    nav = models.FloatField()
    growth = models.FloatField()

    def __str__(self):
        return self.name
