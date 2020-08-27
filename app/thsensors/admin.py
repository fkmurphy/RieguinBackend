from django.contrib import admin

# Register your models here.
from THSensor.models import THSensor

#admin.site.register(Profile)
@admin.register(Controller)
class THSensorAdmin(admin.ModelAdmin):

    list_display=('temp','hum')