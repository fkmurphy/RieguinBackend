from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


import Adafruit_DHT as dht
from users.models import Profile
DHTPIN=4
DHTSENSOR=dht.DHT22

# Create your views here.
def indexHum(request):
    humidity,temperature = dht.read_retry(DHTSENSOR,DHTPIN)
    if humidity is not None and temperature is not None:
        result ="temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity)

    return HttpResponse(result)

@api_view(['GET'])
def viewTemp(request):
    profiles = Profile.objects.all()
    ##la query no se ejecutar hasta usar la variable users (lazyload)
    data = []
    for prof in profiles:
        data.append ({
            'name': prof.user.username        
        })
    #return Response(
    return Response(data)
    #return render(request,'view.html',{'name':'Hola'})
@api_view(['POST'])
def unPost(request):
    name = request.data['name']
    algo = request.data.get('about','')
    data = {
        'name': name,
        'algo': algo
    }
    return Response(data)
