from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Device
from .forms import DeviceForm


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
class ThingsView(DetailView):
    model = Device
    template_name = 'things/device_details.html'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     # form.send_email()
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['row'] = DeviceForm(instance=kwargs['object'])
        return context
    #
    # def post(self, request, **kwargs):
    #     print(self.kwargs)
    #
    #     # if
    #     form = DeviceForm(request.POST)
    #
    #     if form.is_valid():
    #         # записать в базу сразу
    #         # form.device_id =
    #
    #         rec = form.save(commit=False)
    #         rec.device_id = kwargs['pk']
    #         # print(rec)
    #         rec.save()
    #
    #         # # сначала редактирование, потом записать по событию
    #         # new_user = form.save(commit=False)
    #         # new_user.level = 'A'
    #         # new_user.save()
    #         red_url = 'things: index' + str(kwargs['pk']) + '/'
    #         return redirect(red_url)
    #     return render(request, self.template_name, {'form': form})


class ThingsCreate(CreateView):
    model = Device
    fields = ['device_name', 'device_service_date', 'device_model_id', 'device_serial_number', 'device_place_id',
              'device_type_id', 'device_add_date', 'device_part']
    template_name = 'things/device_details.html'


class ThingsUpdate(UpdateView):
    model = Device
    fields = ['device_name', 'device_service_date', 'device_model_id', 'device_serial_number', 'device_place_id',
              'device_type_id', 'device_add_date', 'device_part']
    template_name = 'things/device_details.html'

    def form_valid(self, form):
        print('GOOD')
        return super().form_valid(form)
