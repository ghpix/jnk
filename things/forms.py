from django import forms
# from django.forms import Textarea
from .models import Device


class DeviceEditForm(forms.ModelForm):


    class Meta:
        model = Device
        fields = '__all__'
        # fields = ('device_name', 'device_service_date', 'device_model_id', 'device_serial_number', 'device_place_id',
        #           'device_type_id', 'device_add_date', 'device_part',)
        print(Device.device_name)
        device_name = forms.CharField(max_length=50, )
        device_service_date = forms.DateField(required=False)
        labels = {
            'device_name': 'Dev Name',
            'device_service_date': 'Service date',

        }
        widgets = {
            'device_name': forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                  'placeholder': Device.device_name}),
        }
