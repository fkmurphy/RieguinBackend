# Create your models here.
from django.db import models

class Controller(Component):
        direction = models.CharField(max_length=12,default="out")
