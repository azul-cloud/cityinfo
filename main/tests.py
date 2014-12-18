from django.test import TestCase
from django.core.urlresolvers import reverse

class MainModelTest(TestCase):
    '''
    there are no models that need to be tested in this app
    '''
    pass


class MainViewTest(TestCase):
    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)


class MainFormTest(TestCase):
    pass