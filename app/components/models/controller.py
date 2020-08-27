from components.models import Component
# Create your models here.
class Controller(Component):
        direction = models.CharField(max_length=12,default="out")
