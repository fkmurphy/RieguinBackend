from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from thsensors.models import THSensor
from components.models.sensors import Sensor
from thsensors.serializers import THSensorSerializer

# Create your views here.
@api_view(['GET'])
def view(request,slug):
    sensor = Sensor.objects.get(slug_name=slug)
    dth  = THSensor.create(sensor)
    serializer = THSensorSerializer(dth)
    dth.save()
    data= serializer.data
    return Response(data)
    #return Response(dth.getHum(sensor.gpio.pin))
