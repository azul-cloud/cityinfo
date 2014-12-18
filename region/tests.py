from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.http import urlencode
from django.utils.text import slugify

from .models import Tag, BlogPost
from main.models import User
from region.models import City, Country


class BlogModelTest(TestCase):
    '''
    There are no models that need to be tested in this app
    '''
    pass


