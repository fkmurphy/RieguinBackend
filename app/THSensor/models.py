from django.db import models
from sensors.models import Sensor


# Create your models here.

class THSensor(Sensor):
    hum = models.FloatField(null=False)
    temp = models.FloatField(null=False)
    #is_admin = models.BooleanField(default=False)
    def __str__(self):
        """retorna en formato texto"""
        return "Humedad: "+str(self.hum)+
            " Temperatura: "+str(self.temp)+
            " Fecha: "+str(self.create_at)
