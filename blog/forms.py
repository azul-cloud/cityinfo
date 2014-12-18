from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button

from .models import BlogPost


class BlogPostBaseForm(forms.ModelForm):
    '''
    Base form to be inherited by other blog post forms
    '''
    class Meta:
        model = BlogPost
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(BlogPostBaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            'Create New Post',
            'title',
            'headline',
            'body',
            'tags',
            'city',
            Submit('submit', 'Create Post',
            css_class='text-center')
        )