from django.contrib import admin

# Register your models here.

from .models import Person,UserProfiles

# Register your models here.
admin.site.register(Person)

class UserProfilesAdmin(admin.ModelAdmin):
    list_display=['firstname' ,'lastname' ,'contact' ,
'email' ]
    #search_fields=['firstname' ,'lastname','contact','email']
 
admin.site.register(UserProfiles,UserProfilesAdmin)   
