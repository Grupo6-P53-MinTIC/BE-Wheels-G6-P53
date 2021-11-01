from django.contrib import admin

# Models
from .models.travel import Travel

# Register your models here.

class TravelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'id_manager', 'from_place',
                    'to_place', 'pass_through', 'published', 'date_travel', 'seats', 'price')
    search_fields = ('from_place', 'to_place', 'date_travel')
    list_filter = ('from_place', 'to_place', 'date_travel')

admin.site.register(Travel, TravelAdmin)
