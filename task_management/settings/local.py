from task_management.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': 'taskmanagement',
        'HOST': 'localhost',
        'PORT': 27017

    }
}
