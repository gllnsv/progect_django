from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image', 'get_html_image']
    list_filter = ['auction', 'created_at']

admin.site.register(Advertisements, AdvertisementAdmin)


# Register your models here.
