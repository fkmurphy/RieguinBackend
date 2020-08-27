from django.db import models
from components.models.sensors import Sensor
# Create your models here.
import Adafruit_DHT as dht

DHTSENSOR=dht.DHT22

class THSensor(models.Model):
    hum = models.FloatField(null=False)
    temp = models.FloatField(null=False)
    sensor = models.OneToOneField(
        Sensor,
        on_delete=models.CASCADE,
        related_name="thsensor"
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #is_admin = models.BooleanField(default=False)
    def __str__(self):
        """retorna en formato texto"""
        return "Humedad: "+str(self.hum)+ " Temperatura: "+str(self.temp)+" Fecha: "+str(self.create_at)

    def getHum(self,pin):
        humidity,temperature = dht.read_retry(DHTSENSOR,pin)
        return [humidity,temperature]
        #if humidity is not None and temperature is not None:
        #result ="temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature,humidity)

        #return HttpResponse(result)
