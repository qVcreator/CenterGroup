from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name="home"),
    path('apartments/<int:apartment_id>', ApartmentPage.as_view(), name="apartment"),
]