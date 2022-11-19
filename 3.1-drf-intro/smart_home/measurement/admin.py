from measurement.models import Sensor, Measurement
from django.contrib import admin

# Register your models here.


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'temperature', 'date']