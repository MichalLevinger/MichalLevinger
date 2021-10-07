from django.contrib import admin

from .models import Address
from .models import City
from .models import Country
from .models import Countrylanguage
from .models import Permission
from .models import Person


# Register your models here.

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('type', 'action')
    list_filter = ('type',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    list_per_page = 10


admin.site.register(Address)
admin.site.register(City, CityAdmin)
admin.site.register(Country)
admin.site.register(Countrylanguage)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Person)
