from django.contrib import admin

from .models import Brand, Chassis, CarModel, ECU, Modification

admin.site.register(Brand)
admin.site.register(Chassis)
admin.site.register(CarModel)
admin.site.register(ECU)
admin.site.register(Modification)

