from django import forms
# from django.forms import Textarea
from datetime import datetime
from .models import Device, Model, Manufacturer, Type, Place


class DeviceForm(forms.ModelForm):
    #
    # def get_initial_for_field(self, field, field_name):(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['date'] = Device()
    #     print('##########', context, '##########')
    #     return context

    class Meta:
        model = Device
        fields = '__all__'
        # # fields = ('device_name', 'device_service_date', 'device_model_id', 'device_serial_number', 'device_place_id',
        # #           'device_type_id', 'device_add_date', 'device_part',)
        # # print('!!!!!!!!!!!!', Device, '!!!!!!!!!!!!!')
        #
        # # device_name = forms.CharField(max_length=50, )
        # # device_service_date = forms.DateField(required=False)
        # # device_model_id = forms.ModelChoiceField(Model.objects.all())
        # # device_serial_number = forms.CharField(max_length=50, )
        # # device_place_id = forms.ModelChoiceField(queryset=Place.objects.all())
        # # device_type_id = forms.ModelChoiceField(queryset=Type.objects.all())
        # # device_add_date = forms.DateField(required=False)
        # # device_part = forms.CheckboxInput
        #
        # labels = {
        #     'device_name': 'Dev Name',
        #     'device_service_date': 'Service date',
        #     'device_model_id': 'Model',
        #     'device_serial_number': 'Serial number',
        #     'device_place_id': 'Location',
        #     'device_type_id': 'Device type',
        #     'device_add_date': 'Date added',
        #     'device_part': 'Is a component',
        #     # '': '',
        #     # '': '',
        #
        # }
        # text_css = forms.TextInput(attrs={'class': 'form-control', })
        # date_css = forms.TextInput(attrs={'class': 'form-control',
        #                                   'type': 'date'})
        # checkbox_css = forms.CheckboxInput(attrs={'class': 'form-check-input',
        #                                           'type': 'checkbox'})
        # select_css = forms.Select(attrs={'class': 'form-control'})
        # multiple_select_css = forms.MultipleChoiceField()
        #
        # widgets = {
        #     'device_name': text_css,
        #     'device_service_date': date_css,
        #     'device_model_id': select_css,
        #     'device_serial_number': text_css,
        #     'device_place_id': select_css,
        #     'device_type_id': select_css,
        #     'device_add_date': date_css,
        #     'device_part': checkbox_css,
        # }
        # help_texts = {
        #     '__all__': '',
        #
        # }
