import os, json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django

django.setup()
print("Dajngo module initiated")

from region.models import Country, State, City

data = json.load(open("data.json", encoding="utf8"))
print(len(data))

for i in range(len(data)):
    country_name = data[i]["name"]
    print("Adding Country: ", country_name)
    country_obj = Country(country_name=country_name)
    country_obj.save()
    for j in range(len(data[i]["states"])):
        state_name = data[i]["states"][j]["name"]
        state_obj = State(state_name=state_name, country=country_obj)
        state_obj.save()
        for k in range(len(data[i]["states"][j]["cities"])):
            city_name = data[i]["states"][j]["cities"][k]["name"]
            city_obj = City(city_name=city_name, state=state_obj)
            city_obj.save()
            print(country_name, state_name, city_name)
