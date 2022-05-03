from ._base import *

DEBUG = False
ALLOWED_HOSTS = [
    "*",
]
ADMINS = (
    ('Daniel', 'monkaS123123@gmail.com')
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elearning',
        'USER': 'elearning',
        'PASSWORD': '1111',
    }
}
