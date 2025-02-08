from .base import *

SECRET_KEY = 'django-insecure--wk1&rkp6d(%io_k%x=j02c9i4ix+x=ggov!yg^8%hx0o1%bc#'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'