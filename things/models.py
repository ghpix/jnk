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


class Device(models.Model):
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=50)
    device_place_id = models.ForeignKey(Place, on_delete=models.CASCADE, )
    device_type_id = models.ForeignKey(Type, on_delete=models.CASCADE, )
    device_refillable = models.BooleanField()
