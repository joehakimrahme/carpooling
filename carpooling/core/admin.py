from django.contrib import admin

# Register your models here.
from carpooling.core.models import Ad, Location

admin.site.register(Location)
admin.site.register(Ad)
