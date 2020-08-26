from django.db import models

# Create your models here.

class Component(models.Model):
    name = models.TextField(max_length=200,unique=True)
    pin_number = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
