from django.shortcuts import render
from django.http import HttpResponse
from pigpio_dht import DHT22
 
GPIO=4
SENSOR=DHT22(GPIO)

# Create your views here.
def index(request):
    result = sensor.read()

    return HttpResponse("Hello, world. You're at the polls index."+result)