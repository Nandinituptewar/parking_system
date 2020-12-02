from django.contrib import admin
from django.contrib import admin
from . import apps
from .models  import Person,park_area_data,slot_description

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name','plate_num','status','time_1')
    search_fields = ('id',)
    list_filter = ('time_1',)

class Park_area_dataAdmin(admin.ModelAdmin):
    list_display = ('id','slots',)

class slot_descriptionAdmin(admin.ModelAdmin):
    list_display = ('capacity','description',)


admin.site.site_header='Parking System Dashboard'
admin.site.register(Person,PersonAdmin)
admin.site.register(park_area_data,Park_area_dataAdmin)
admin.site.register(slot_description,slot_descriptionAdmin)
#https://django-fluent-contents.readthedocs.io/en/latest/newplugins/admin.html

