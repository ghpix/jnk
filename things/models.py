from django.db import models


# Create your models here.


class Place(models.Model):
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    place_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=50)


class Type(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)


class Manufacturer(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    manufacturer_id = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=50)


class Model(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    model_id = models.AutoField(primary_key=True)
    model_manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, )
    model_name = models.CharField(max_length=50)


class Device(models.Model):
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=50)
    device_service_date = models.DateField()
    device_model_id = models.ForeignKey(Model, on_delete=models.CASCADE, )
    device_place_id = models.ForeignKey(Place, on_delete=models.CASCADE, )
    device_type_id = models.ForeignKey(Type, on_delete=models.CASCADE, )
    device_refillable = models.BooleanField()
