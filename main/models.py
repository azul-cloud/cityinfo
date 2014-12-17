from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
	'''
	An abstract base class model that provides selfupdating
	created and modified fields.
	'''
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True


class User(AbstractUser):
    '''
    Our custom user class
    '''
    contributor = models.NullBooleanField(default=False)