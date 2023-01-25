from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name="home"),
    path('apartment/<int:apartment_id>', apartment_page, name="apartment"),
]