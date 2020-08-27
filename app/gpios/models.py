from django.db import models

# Create your models here.
class Gpio(models.Model):
    enable = models.BooleanField()
    pin = models.PositiveSmallIntegerField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    