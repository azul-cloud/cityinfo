from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import BlogPost


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
