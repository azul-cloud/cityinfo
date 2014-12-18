from .models import City, Country


def main(request):
    city_list = City.objects.all()
    country_list = Country.objects.all()

    return {'country_list': country_list, 
            'city_list': city_list}