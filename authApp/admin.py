from django.contrib import admin

# Models
from .models.user import User
from .models.manager import Manager

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id','name', 'city')
    search_fields = ('id','name', 'last_name')
    list_filter = ('id', 'city')

class ManagerAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'car_type', 'is_active')
    search_fields = ('car_type', 'is_active')
    list_filter = ('is_active', 'car_type')


admin.site.register(User, UserAdmin)
admin.site.register(Manager, ManagerAdmin)