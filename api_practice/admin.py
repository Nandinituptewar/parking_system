from django.contrib import admin
from .models import Movie,Rating

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','description',)
    search_fields = ('title',)
    list_filter = ('title',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie','user','stars',)
    search_fields = ('stars',)

admin.site.register(Movie,MovieAdmin)
admin.site.register(Rating,RatingAdmin)
