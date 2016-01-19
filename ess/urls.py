from django.conf.urls import url

from ess.views import BrandListView, ChassisListView, CarModelListView, ECUListView, ModificationListView, \
    ModificationDetailView

urlpatterns = [
    url('^$', BrandListView.as_view(), name='brand-list'),
    url('^(?P<brand>\w+)/$', ChassisListView.as_view(), name='chassis-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/$', CarModelListView.as_view(),
        name='car-model-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/(?P<car_model>[\w\.]+)/$', ECUListView.as_view(), name='ecu-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/(?P<car_model>[\w\.]+)/(?P<ecu>\w+)/$', ModificationListView.as_view(),
        name='modification-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/(?P<car_model>[\w\.]+)/(?P<ecu>\w+)/(?P<modification>\w+)$',
        ModificationDetailView.as_view(),
        name='modification-detail'),

]
