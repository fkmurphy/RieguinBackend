from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def view(request,slug):
    dht = THSensor.objects.filter(slug=slug)
    
    return Response(dht.getHum())