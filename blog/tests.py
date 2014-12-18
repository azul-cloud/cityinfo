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
            "testpassword",
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


class BlogViewTest(TestCase):
    def setUp(self):
        BlogModelTest.setUp(self)

        self.client.login(username=self.user.username, 
            password='testpassword')

    def test_blog_home(self):
        url = reverse('blog_home')
        response = self.client.get(url)

        self.assertContains(response, "City Info")

    def test_blog_create(self):
        url = reverse('blog_create')
        response = self.client.get(url)

        self.assertContains(response, "Create")

    def test_blog_update(self):
        url = reverse('blog_update', kwargs={'slug':self.post.slug})
        response = self.client.get(url)

        self.assertContains(response, "Update")

    def test_blog_post(self):
        url = reverse('blog_post', kwargs={'slug':self.post.slug})
        response = self.client.get(url)

        self.assertContains(response, self.post.title)

    def test_blog_search(self):
        '''
        this is just testing the search view, it is not testing the
        functionality of the search form, nor the results.
        '''
        url = reverse('blog_search')
        response = self.client.get(url)


class BlogFormTest(TestCase):
    pass

