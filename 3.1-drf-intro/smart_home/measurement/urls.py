from django.urls import path
from measurement.views import SensorsView, OneSensorView, CreateMeasurement


urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
