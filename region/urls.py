from django.urls import path
from .views import fetchCountries, fetchStates, fetchCities

urlpatterns = [
    path("fetchCountries/", fetchCountries),
    path("fetchStates/", fetchStates),
    path("fetchCities/", fetchCities),
]
