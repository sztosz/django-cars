from django.views.generic import ListView, DetailView

from .models import Brand, Chassis, CarModel, ECU, Modification


class BrandListView(ListView):
    model = Brand


class ChassisListView(ListView):
    model = Chassis

    def get_queryset(self):
        return Chassis.objects.filter(brand__name=self.kwargs['brand'])


class CarModelListView(ListView):
    model = CarModel

    def get_queryset(self):
        return CarModel.objects.filter(
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
        return Modification.objects.all().filter(
            ecu__car_model__chassis__brand__name=self.kwargs['brand']).filter(
            ecu__car_model__chassis__name=self.kwargs['chassis']).filter(
            ecu__car_model__name=self.kwargs['car_model']).filter(
            ecu__name=self.kwargs['ecu']).filter(
            name=self.kwargs['modification']).first(

        )
