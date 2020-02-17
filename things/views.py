from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Device
from django.urls import reverse_lazy
from .forms import DeviceForm


# show all devices
class ThingsList(ListView):
    model = Device
    template_name = 'things/index.html'
    context_object_name = 'device_list'

    # # # todo Filter !!!
    # def get_context_data(self, **kwargs):
    #     queryset = super().get_queryset
    #     queryset = queryset.filter(device_id=1)
    #     return queryset


# # show one device details
# # class ThingsView(DetailView):
# #     model = Device
# #     template_name = 'things/view_edit_thing.html'
# #
# #     queryset = Device.objects.all()
# #
# #     def get_object(self):
# #         obj = super().get_object()
# #         return obj
#
#
# class ThingsView(FormView):
#     model = Device
#     template_name = 'things/view_edit_thing.html'
#     form_class = DeviceForm
#     # queryset = Device.objects.all()
#
#
#     # def get_queryset(self):
#     #     return Device.objects.all()
#     #
#     # def get_initial(self):
#     #     initial = super(DeviceForm, self).get_initial()
#     #     return initial
#     #
#     # def get_form_kwargs(self):
#     #     kwargs = super(DeviceForm, self).get_form_kwargs()
#     #     kwargs.update({'user': self.request.user})
#     #
#     # def form_valid(self, form):
#     #     return super(DeviceForm, self).form_valid(form)


class ThingCreate(CreateView):
    model = Device
    fields = ['device_name', 'device_service_date', 'device_model_id', 'device_serial_number', 'device_place_id',
              'device_type_id', 'device_add_date', 'device_part']
    template_name = 'things/create_thing.html'


class ThingView(UpdateView):
    model = Device
    fields = ['device_name', 'device_service_date', 'device_model_id', 'device_serial_number', 'device_place_id',
              'device_type_id', 'device_add_date', 'device_part']
    template_name = 'things/view_edit_thing.html'

    def form_valid(self, form):
        print('GOOD')
        return super().form_valid(form)


class ThingDelete(DeleteView):
    model = Device
    success_url = reverse_lazy('things:index')
    template_name = 'things/delete_thing.html'
