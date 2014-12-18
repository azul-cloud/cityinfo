from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    '''
    An abstract base class model that provides selfupdating
    created and modified fields.
    '''
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


# class SaveSlug(models.Model, **kwargs)

#     field_name = kwargs['field_name']

#     if field_name = "name":
#         name = models.CharField(max_length=30)

#     elif field_name = "title":
#         title = models.CharField(max_length=30)
    
#     slug = models.SlugField(db_index=True, unique=True)

#     def save(self, *args, **kwargs):
#         # add identifying slug field on save
#         self.slug = slugify(self.name)

#         super(SaveSlug, self).save(*args, **kwargs)    

#     class Meta:
#         abstract = True


class User(AbstractUser):
    '''
    Extended User class
    '''
    contributor = models.NullBooleanField(default=False)


class Country(models.Model):
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

    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField()
    continent = models.CharField(max_length=15, choices=CONTINENT_CHOICES)

    def __str__(self):
        return self.name


class City(models.Model):
    '''
    City objects will allow us to group items (such as blog posts,
    events, etc) by city.
    '''

    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField()
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name + ', ' + self.country.name

    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.name)

        super(City, self).save(*args, **kwargs)



