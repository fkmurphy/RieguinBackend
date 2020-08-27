from django.db import models
class Sensor(Component):
        direction = models.CharField(max_length=12,default="in")
