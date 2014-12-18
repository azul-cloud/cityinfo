from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, \
    UpdateView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import BlogPost
from .forms import BlogPostCreateForm, BlogPostUpdateForm


class BlogHomeTemplateView(TemplateView):
    '''
    Shows the homepage for all blogs. Not sure what this page is going
    to be doing yet.
    '''

    template_name = "blogcontent/home.html"


class BlogPostDetailView(DetailView):
    '''
    Performs the logic for showing a single blog post
    '''

    model = BlogPost
    template_name = "blogcontent/post.html"


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates a new blog post
    '''

    model = BlogPost
    form_class = BlogPostCreateForm
    template_name = "blogcontent/create.html"

    def form_valid(self, form):
        '''
        set fields that aren't on the form
        '''
        form.instance.author = self.request.user
        return super(BlogPostCreateView, self).form_valid(form)


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    '''
    Updates a blog post
    '''

    model = BlogPost
    form_class = BlogPostUpdateForm
    template_name = "blogcontent/update.html"

