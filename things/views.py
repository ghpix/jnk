from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Device


@require_http_methods(['GET', 'POST'])
def things_index(request):
    device = Device.objects.all()
    args = {
        'device': device,
        'test': list(range(1, 11)),  # например список 10 чисел
    }
    response = render(request, 'things/index.html', args)
    return response


def things_id(request, device_id):
    device = Device.objects.all()
    args = {
        'device': device,
        'test': list(range(1, 11)),  # например список 10 чисел
    }
    response = render(request, 'things/device_details.html', args)
    return response


# show all devices
class ThingsList(ListView):
    model = Device
    template_name = 'things/index.html'
    context_object_name = 'device_list'

    # # todo Filter !!!
    def get_context_data(self, **kwargs):
        queryset = super().get_queryset
        queryset = queryset.filter(device_id=1)
        return queryset


# show one device details
class ThingsId(DetailView):
    model = Device
    template_name = 'things/device_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
