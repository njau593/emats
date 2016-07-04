from django.contrib import admin
from .models import aboutUs, service, keProfile
from .models import postInfo, reachUs

# Register your models here.

admin.site.register(aboutUs)
admin.site.register(service)
admin.site.register(keProfile)
admin.site.register(postInfo)
admin.site.register(reachUs)
