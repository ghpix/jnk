from django.contrib import admin

# Register your models here.


from .models import Place, Device, Type, Manufacturer, Model, Param

'''
device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=50, unique=True)
    device_serial_number = models.CharField(max_length=50, unique=True, default=datetime.now())
    device_service_date = models.DateField(default=datetime.now())
    device_model_id = models.ForeignKey(Model, on_delete=models.CASCADE, default=None)
    device_place_id = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)
    device_type_id = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    device_refillable = models.BooleanField()
'''


@admin.register(Device)
class ThingsAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'device_name', 'device_serial_number', 'device_service_date', 'device_add_date',)
    list_display_links = ('device_id', 'device_name', 'device_serial_number', 'device_service_date','device_add_date',)
    empty_value_display = 'not stated'


admin.site.register(Place)
# admin.site.register(Device)
admin.site.register(Type)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(Param)
