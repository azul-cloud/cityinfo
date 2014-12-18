from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from main.models import TimeStampedModel, City


class Tag(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-tag', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.name)

        super(Tag, self).save(*args, **kwargs)


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=40)
    slug = models.SlugField(db_index=True, blank=True, editable=False)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)
    city = models.ForeignKey(City)

    class Meta:
        unique_together = ("city", "slug")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.title)

        super(BlogPost, self).save(*args, **kwargs)




