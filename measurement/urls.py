from django.urls import path
from .views import SensorsList, SensorView, MeasurementDetail, MeasurementView


urlpatterns = [
    path('sensor/', SensorsList.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('measurement/<pk>/', MeasurementDetail.as_view()),
]