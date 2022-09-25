from django.http import JsonResponse
from django.shortcuts import render
from .models import Country, State

# Create your views here.
def fetchCountries(request):
    d = {}
    for country in Country.objects.all():
        d[country.id] = country.country_name
    return JsonResponse(d, safe=False)


def fetchStates(request):
    d = {}
    country_id = int(request.GET["country_id"])
    if Country.objects.filter(id=country_id):
        country = Country.objects.get(id=country_id)
        d["country"] = country.country_name
        d["states"] = []
        for state in country.state_set.all():
            d["states"].append({state.id: state.state_name})
        return JsonResponse(d, safe=False)
    else:
        return JsonResponse({"error": "COuntry ID doesn't exist"})


def fetchCities(request):
    d = {}
    state_id = int(request.GET["state_id"])
    if State.objects.filter(id=state_id):
        state = State.objects.get(id=state_id)
        d["state"] = state.state_name
        d["cities"] = []
        for city in state.city_set.all():
            d["cities"].append({city.id: city.city_name})
        return JsonResponse(d, safe=False)
    else:
        return JsonResponse({"error": "State ID doesn't exist"})
