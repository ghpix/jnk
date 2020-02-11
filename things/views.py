from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
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


