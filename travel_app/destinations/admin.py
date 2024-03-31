from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name','country','description','best_time_to_visit','category','image_url','created_at','updated_at']
