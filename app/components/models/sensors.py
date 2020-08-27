from django.db import models
from components.models.components import Component
class Sensor(Component):
        direction = models.CharField(max_length=12,default="in")
