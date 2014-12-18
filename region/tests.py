from django.test import TestCase
from django.core.urlresolvers import reverse

from blog.tests import BlogModelTest


class RegionModelTest(TestCase):
    '''
    There are no models that need to be tested in this app
    '''
    pass


class RegionViewTest(TestCase):
    def setUp(self):
        BlogModelTest.setUp(self)

    def test_city(self):
        url = reverse('region_city', kwargs={'slug':self.city.slug})
        response = self.client.get(url)

        self.assertContains(response, self.city.name)

    def test_country(self):
        url = reverse('region_country', kwargs={'slug':self.country.slug})
        response = self.client.get(url)

        self.assertContains(response, self.country.name)


class RegionFormTest(TestCase):
    pass