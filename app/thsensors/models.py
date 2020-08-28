from django.db import models
from components.models.sensors import Sensor
from gpios.models import Gpio
# Create your models here.
import Adafruit_DHT as dht

DHTSENSOR=dht.DHT22

class THSensor(models.Model):
    hum = models.FloatField(null=False)
    temp = models.FloatField(null=False)
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="thsensor"
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    @classmethod
    def create(cls,sensor):
        #self.sensor = Gpio.objects.get(pin=pin).sensor
        humidity,temperature = dht.read_retry(DHTSENSOR,sensor.gpio.pin)
        thsensor = cls(sensor=sensor,hum=humidity,temp=temperature)
        return thsensor

    #is_admin = models.BooleanField(default=False)
    def __str__(self):
        """retorna en formato texto"""
        return "Humedad: "+str(self.hum)+ " Temperatura: "+str(self.temp)+" Fecha: "+str(self.create_at)
