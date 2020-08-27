from django.contrib import admin

# Register your models here.
from gpios.models import Gpio

#admin.site.register(Profile)
@admin.register(Gpio)
class GpioAdmin(admin.ModelAdmin):

    list_display=('pin','enable')
