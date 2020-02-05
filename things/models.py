from django.db import models
from datetime import datetime, date


# Create your models here.


class Place(models.Model):
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=50, unique=True, default=None)

    def __str__(self):
        return f'{self.place_name}'


class Type(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.type_name}'


class Manufacturer(models.Model):
    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    manufacturer_id = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.manufacturer_name}'


class Model(models.Model):
    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=50, unique=True)
    model_manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.model_name}'


class Device(models.Model):
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    # _make_sn my company default serial number format DDMMYYNUM   - NUM > number 00-99
    @staticmethod
    def _make_sn():
        date_str = datetime.now().strftime('%d%m%y')
        obj = Device.objects.filter(device_serial_number__startswith=date_str)
        today_count = 1 + obj.count()
        return date_str + "%02d" % today_count

    # @staticmethod
    # def get_date_f(self):
    #     return date.today().strftime('%D-%M-%Y')

    device_sn = _make_sn.__get__(object)

    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=50, unique=True)
    device_serial_number = models.CharField(max_length=50, unique=True, default=device_sn)
    device_service_date = models.DateField(default=datetime.now())
    device_add_date = models.DateField(default=datetime.now())
    device_model_id = models.ForeignKey(Model, on_delete=models.CASCADE, default=None)
    device_place_id = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)
    device_type_id = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    device_refillable = models.BooleanField()

    def __str__(self):
        return f'{self.device_id} {self.device_name} {self.device_serial_number} {self.device_service_date} ' \
               f'{self.device_add_date}'


class Param(models.Model):
    class Meta:
        verbose_name = 'Param'
        verbose_name_plural = 'Params'

    param_id = models.AutoField(primary_key=True)
    param_name = models.CharField(max_length=50, unique=True)
    model_manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.param_name}'
