from django.contrib import admin

# Register your models here.


from .models import Place, Device, Type

admin.site.register(Place)
admin.site.register(Device)
admin.site.register(Type)