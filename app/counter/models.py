from django.db import models

# Create your models here.
class CounterModel(models.Model):
    number = models.IntegerField(default=0)