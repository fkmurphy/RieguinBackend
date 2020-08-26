from django.db import models

# Create your models here.

class THSensor(models.Model):
    hum = models.FloatField(null=False)
    temp = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #is_admin = models.BooleanField(default=False)
    def __str__(self):
        """retorna en formato texto"""
        return "Humedad: "+str(self.hum)+" Temperatura: "+str(self.temp)+" Fecha: "+str(self.create_at)
