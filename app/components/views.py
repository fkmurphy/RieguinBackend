from django.shortcuts import render

from django.http import HttpResponse
import time
from os import path

# Create your views here.
RELEEPINS=[2,3]
PATH="/sys/class/gpio/"
def index(requests):
    #preparar start(2) 
    time.sleep(2)
    return HttpResponse("down up or status")

def preparePins(requests):
    f = open(PATH+"export",'w')
    message=""
    for i in RELEEPINS:
        if (not path.exists(PATH+"gpio"+str(i)+"/")):
            message+="Activate pin: "+str(i)+"<br>"
            f.write(str(i)) 
        else:
            message+="Pin exist: "+str(i)+"<br>"
    f.close()
    
    return HttpResponse(message)

def start(requests,pin):
    f = open(PATH+"gpio"+str(pin)+"/direction",'w')
    f.write("out")
    f.close()
    return HttpResponse("Listo!")

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
    msg="<p>Está encendido</p>"
    if(0 == int(value)):
        msg="<p>No está encendido</p>"
    return HttpResponse(msg)

