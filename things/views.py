from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def things_index(request):
    args = {
        'test': list(range(1, 11)),  # например список 10 чисел
    }
    response = render(request, 'things/index.html', args)
    return response
