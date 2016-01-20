from django.contrib import admin

from .models import Brand, Chassis, Engine, ECU, Modification

admin.site.register(Brand)
admin.site.register(Chassis)
admin.site.register(Engine)
admin.site.register(ECU)
admin.site.register(Modification)

