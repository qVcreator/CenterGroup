from django.contrib import admin

from .models import *

admin.site.register(Apartment)
admin.site.register(ApartmentPhotos)
admin.site.register(Comment)

