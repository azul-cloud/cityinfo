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


class SaveSlugBase(models.Model):
    '''
    Base class to create a slugfield
    '''

    slug = models.SlugField(db_index=True, unique=True, 
        editable=False, blank=True)

    def save(self, *args, **kwargs):
        '''
        Check which field is on the model. We either base the
        slug off of the title or name field.
        '''
        if hasattr(attr, 'title'):
            self.slug = slugify(self.title)
        elif hasattr(attr, 'name'):
            self.slug = slugify(self.name)

        super(SaveSlugBase, self).save(*args, **kwargs)    

    class Meta:
        abstract = True


class SaveSlugTitle(SaveSlugBase):
    '''
    create a title field with the autosave slug field
    '''
    title = models.CharField(max_length=40)

    class Meta:
        abstract = True


class SaveSlugName(SaveSlugBase):
    '''
    create a name field with the autosave slug field
    '''
    name = models.CharField(max_length=40)

    class Meta:
        abstract = True


class User(AbstractUser):
    '''
    Extended User class
    '''
    contributor = models.NullBooleanField(default=False)



