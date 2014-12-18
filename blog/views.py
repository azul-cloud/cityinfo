from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, \
    UpdateView, ListView
from django.core.urlresolvers import reverse
from django.db.models import Q

from braces.views import LoginRequiredMixin

from .models import BlogPost
from .forms import BlogPostCreateForm, BlogPostUpdateForm


class BlogHomeTemplateView(TemplateView):
    '''
    Shows the homepage for all blogs. Not sure what this page is going
    to be doing yet.
    '''

    template_name = "blogcontent/home.html"


class BlogPostListView(ListView):
    '''
    return a list of blog posts
    '''
    model = BlogPost


class BlogPostDetailView(DetailView):
    '''
    Performs the logic for showing a single blog post
    '''
    model = BlogPost
    template_name = "blogcontent/post.html"


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    '''
    Creates a new blog post. We will submit the form without
    the author field and then assign the logged in user
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


class BlogSearchListView(BlogPostListView):
    '''
    Search for blog posts
    '''
    template_name = "blogcontent/search.html"

    def get_queryset(self):
        '''
        if we searched for something, filter the queryset. If not,
        just return the default queryset
        '''
        queryset = super(BlogSearchListView, self).get_queryset()
        
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        else:
            return queryset




