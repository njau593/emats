from django.contrib import admin
from .models import detailedService, service

# Register your models here.

admin.site.register(service)
admin.site.register(detailedService)
