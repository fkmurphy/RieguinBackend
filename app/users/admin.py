from django.contrib import admin

##import
from users.models import Profile


# Register your models here.

#admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display=('user','website')
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
