from django.contrib import admin

# Register your models here.
from thsensors.models import THSensor

#admin.site.register(Profile)
@admin.register(THSensor)
class THSensorAdmin(admin.ModelAdmin):

    list_display=('temp','hum')
