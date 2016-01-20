from django.http import HttpResponse, FileResponse
from django.views.generic import ListView, DetailView, View

from .models import Brand, Chassis, Engine, ECU, Modification
from .forms import UploadForm


class BrandListView(ListView):
    model = Brand


class ChassisListView(ListView):
    model = Chassis

    def get_queryset(self):
        return Chassis.objects.filter(brand__name=self.kwargs['brand'])


class EngineListView(ListView):
    model = Engine

    def get_queryset(self):
        return Engine.objects.filter(
            chassis__brand__name=self.kwargs['brand']).filter(
            chassis__name=self.kwargs['chassis'])


class ECUListView(ListView):
    model = ECU

    def get_queryset(self):
        return ECU.objects.filter(
            car_model__chassis__brand__name=self.kwargs['brand']).filter(
            car_model__chassis__name=self.kwargs['chassis']).filter(
            car_model__name=self.kwargs['car_model']
        )


class ModificationListView(ListView):
    model = Modification

    def get_queryset(self):
        return Modification.objects.all().filter(
            ecu__car_model__chassis__brand__name=self.kwargs['brand']).filter(
            ecu__car_model__chassis__name=self.kwargs['chassis']).filter(
            ecu__car_model__name=self.kwargs['car_model']).filter(
            ecu__name=self.kwargs['ecu']
        )


class ModificationDetailView(DetailView):
    model = Modification

    def get_object(self, queryset=None):
        return Modification.objects.filter(
            ecu__car_model__chassis__brand__name=self.kwargs['brand']).filter(
            ecu__car_model__chassis__name=self.kwargs['chassis']).filter(
            ecu__car_model__name=self.kwargs['car_model']).filter(
            ecu__name=self.kwargs['ecu']).filter(
            name=self.kwargs['modification']).get(
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UploadForm
        return context


class ModificationFileUploadView(View):
    form_class = UploadForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            script = Modification.objects.filter(
                ecu__car_model__chassis__brand__name=self.kwargs['brand']).filter(
                ecu__car_model__chassis__name=self.kwargs['chassis']).filter(
                ecu__car_model__name=self.kwargs['car_model']).filter(
                ecu__name=self.kwargs['ecu']).filter(
                name=self.kwargs['modification']).get(
            ).script
            temp_env = {}
            exec(script, temp_env)
            content = request.FILES['file'].file.read()
            content, message, error = temp_env['make_change'](content)
            response = HttpResponse(content_type='application/octet-stream', content=content)
            response["Content-Disposition"] = "attachment; filename=changed_{}".format(request.FILES['file'].name)
            return response
