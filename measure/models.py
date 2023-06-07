from django.db import models
# from djongo import models

# Create your models here.
class SoilMeasurement(models.Model):
    location_x = models.FloatField(default=0.0)
    location_y = models.FloatField(default=0.0)
    drilled_status = models.BooleanField(default=True)
    ph_current = models.FloatField(default=0.0)
    ph_value = models.FloatField(default=0.0)
    nitrogen_sensor = models.FloatField(default=0.0)
    nitrogen_reading = models.FloatField(default=0.0)
    phosphorous_sensor = models.FloatField(default=0.0)
    phosphorous_reading = models.FloatField(default=0.0)
    potassium_sensor = models.FloatField(default=0.0)
    potassium_reading = models.FloatField(default=0.0)
    measurement_date = models.DateTimeField()

    def __str__(self):
        return str(self.measurement_date)
    
class FieldData(models.Model):
    fieldLength = models.FloatField(default=0.0)
    fieldWidth = models.FloatField(default=0.0)
    numberOfReadings = models.IntegerField(default=0)

    def __str__(self):
        return "Field Length: {} Field Width: {} Number Of Readings: {}".format(self.fieldLength, self.fieldWidth, self.numberOfReadings)