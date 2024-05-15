from django.db import models

# Create your models here.
class Criteria(models.Model):
    parameter = models.CharField(max_length=100)
    operator = models.CharField(max_length=2, choices=[('<', '<'), ('>', '>'), ('<=', '<='), ('>=', '>='), ('==', '==')])
    threshold = models.FloatField()
    frequency = models.CharField(max_length=10, choices=[('day', 'Day'), ('month', 'Month'), ('year', 'Year')])

class WeatherData(models.Model):
    parameter = models.CharField(max_length=100)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
