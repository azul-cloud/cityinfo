from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.http import urlencode
from django.utils.text import slugify

from .models import Tag, BlogPost
from main.models import User
from region.models import City, Country


class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "test_user",
            "email@domain.com",
            "testpasswd",
        )

        self.country = Country.objects.create(
            continent="South America",
            name="Colombia"
        )
        self.city = City.objects.create(
            name="Medellin",
            country=self.country
        )

        self.tag1 = Tag.objects.create(
            name = "Tag 1"
        )
        self.tag2 = Tag.objects.create(
            name = "Tag 2"
        )

        self.post = BlogPost.objects.create(
            title = "Test Title",
            headline = "This is my test headline",
            body = "<h1>Hello Test World</h1>",
            author = self.user,
            city = self.city
        )

    def test_tag(self):
        # select the tags and ensure they have slugs
        tag = Tag.objects.get(name = "Tag 1")
        self.assertNotEqual(tag.slug, None)

    def test_blog_post(self):
        # select the blog post and ensure it has its slug
        post = BlogPost.objects.get(title="Test Title")
        self.assertNotEqual(post.slug, None)


