from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_django_tutorial",
        "USER": "tutorial_app_tester",
        "PASSWORD": "verysecret",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}