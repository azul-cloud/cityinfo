from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model


admin.site.register(get_user_model())