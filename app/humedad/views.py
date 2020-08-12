from django.shortcuts import render
from django.http import HttpResponse
import Adafruit_DHT as dht

DHTPIN=4
DHTSENSOR=dht.DHT22

# Create your views here.
def index(request):
    humidity,temperature = dht.read_retry(DHTSENSOR,DHTPIN)
    if humidity is not None and temperature is not None:
        result ="temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity)

    return HttpResponse("Hello, world. You're at the polls aindex."+result)
