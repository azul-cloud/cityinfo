from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, ButtonHolder

from .models import BlogPost


class BlogPostBaseForm(forms.ModelForm):
    '''
    Base form to be inherited by other blog post forms
    '''

    # set the text at the top of the form
    form_title = ""

    class Meta:
        model = BlogPost
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(BlogPostBaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                self.form_title,
                'title',
                'headline',
                'body',
                'tags',
                'city',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )


class BlogPostCreateForm(BlogPostBaseForm):
    '''
    Create a new blog post
    '''

    form_title = "<h1 class='text-center'>Create New Post</h1>"


class BlogPostUpdateForm(BlogPostBaseForm):
    '''
    Update an existing blog post
    '''

    form_title = "<h1 class='text-center'>Update Blog Post</h1>"

