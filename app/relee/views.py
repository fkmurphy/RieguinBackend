from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
RELEEPINS=[2,3]
PATH="/sys/class/gpio/"
def index(requests):
    #preparar start(2) 
    time.sleep(2)
    return HttpResponse("down up or status")

def start(pin):
    f = open(PATH+"gpio"+str(pin)+"/direction",'w')
    f.write("out")
    f.close()

def down(requests,pin):
    f = open(PATH+"gpio"+str(pin)+"/value",'w')
    f.write("1")
    f.close()
    return HttpResponse("Listo!")
def up(requests,pin):
    f = open(PATH+"gpio"+str(pin)+"/value",'w')
    f.write("0")
    f.close()
    return HttpResponse("Listo!")
def status(requests,pin):
    f = open(PATH+"gpio"+str(pin)+"/value",'r')
    value = f.read()
    f.close()
    msg="<p>No está encendido</p>"
    if(0 == int(value)):
        msg="<p>Está encendido</p>"
    return HttpResponse(msg)

