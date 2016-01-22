from django.conf.urls import url

from ess.views import BrandListView, ChassisListView, EngineListView, ECUListView, ModificationListView, \
    ModificationDetailView, ModificationFileUploadView

urlpatterns = [
    url('^$', BrandListView.as_view(), name='brand-list'),
    url('^(?P<brand>\w+)/$', ChassisListView.as_view(), name='chassis-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/$', EngineListView.as_view(),
        name='car-model-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/(?P<car_model>[\w\.]+)/$', ECUListView.as_view(), name='ecu-list'),
    url('^(?P<brand>\w+)/(?P<chassis>\w+)/(?P<car_model>[\w\.]+)/(?P<ecu>\w+)/$', ModificationListView.as_view(),
        name='modification-list'),
    url('^modification/(?P<id>\d+)$',
        ModificationDetailView.as_view(),
        name='modification-detail'),
    url('^modification/(?P<id>\d+)$',
        ModificationFileUploadView.as_view(),
        name='modification-upload'),

]
