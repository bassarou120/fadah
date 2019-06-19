
import dj_database_url
from .settings import *


DEBUG = False
TEMPLATE_DEBUG=False

ALLOWED_HOSTS = ['fadahtech.herokuapp.com']

SECRET_KEY = 'y_3nim**kz(xxdjvdx0l!ld(s@mp3eng-b3d^em$**v2s43pt0'

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE +=['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'