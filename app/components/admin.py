from django.contrib import admin

##import
from components.models.controllers import Controller
from components.models.sensors import Sensor

#admin.site.register(Profile)
@admin.register(Controller)
class ControllerAdmin(admin.ModelAdmin):

    list_display=('gpio','name','description')
    #list_display_links =
    #list_editable =
    #search_fields = ('user__email','user__last_name')
    #list_filter = ('created')

    """
    fieldsets = (
        
        ('Profile',{
            'fields': ('user','picture'),
        }),
    )
    """
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):

    list_display=('gpio','name','description')