
# Create your models here.
# iot_app/models.py

from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    gaz = models.FloatField(default=0.0)
    wind = models.FloatField(default=0.0)
    air = models.FloatField(default=0.0)
