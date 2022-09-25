from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=500, unique=True)

    def __str__(self) -> str:
        return self.country_name


class State(models.Model):
    state_name = models.CharField(max_length=500)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.city_name
