from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name="home"),
    path('apartment/<int:apartment_id>', apartment_page, name="apartment"),
]