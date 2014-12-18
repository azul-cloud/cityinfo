from django.shortcuts import render
from django.views.generic import ListView


from .models import City, Country


class CityListView(ListView):
    '''
    Homepage for a city
    '''
    model = City
    template_name = "regioncontent/city.html"


class CountryListView(ListView):
    '''
    Homepage for a country
    '''
    model = Country
    template_name = "regioncontent/country.html"
