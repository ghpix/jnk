from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Device
from .forms import DeviceEditForm


# @require_http_methods(['GET', 'POST'])
# def things_index(request):
#     device = Device.objects.all()
#     args = {
#         'device': device,
#         'test': list(range(1, 11)),  # например список 10 чисел
#     }
#     response = render(request, 'things/index.html', args)
#     return response
#
#
# def things_id(request, device_id):
#     device = Device.objects.all()
#     args = {
#         'device': device,
#         'test': list(range(1, 11)),  # например список 10 чисел
#     }
#     response = render(request, 'things/device_details.html', args)
#     return response


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


# show one device details
class ThingsId(DetailView):
    model = Device
    template_name = 'things/device_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeviceEditForm()
        print(context)
        return context

    def post(self, request):
        # print(request.POST)
        form = DeviceEditForm(request.POST)
        if form.is_valid():
            # записать в базу сразу
            form.save()

            # # сначала редактирование, потом записать по событию
            # new_user = form.save(commit=False)
            # new_user.level = 'A'
            # new_user.save()
            return redirect('things:index/')
        return render(request, self.template_name, {'form': form})
