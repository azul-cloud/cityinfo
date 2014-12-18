from django.db import models
from django.utils.text import slugify

from main.models import SaveSlugName


class Country(SaveSlugName):
    '''
    Separate model for Country so that we can have data specific
    to a country, such as continent. This allows for more detailed
    info on countries, as well as grouping by country/continent
    '''

    CONTINENT_CHOICES = (
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe')
    )

    continent = models.CharField(max_length=15, choices=CONTINENT_CHOICES)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return self.slug


class City(SaveSlugName):
    '''
    City objects will allow us to group items (such as blog posts,
    events, etc) by city.
    '''

    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name + ', ' + self.country.name

    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.name)

        super(City, self).save(*args, **kwargs)