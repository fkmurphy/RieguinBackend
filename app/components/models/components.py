from django.db import models
from gpios.models import Gpio
# Create your models here.

class Component(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField()
    direction = models.CharField(max_length=12)
    gpio = models.OneToOneField(
        Gpio,
        on_delete=models.CASCADE
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
