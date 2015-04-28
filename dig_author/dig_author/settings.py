"""
Django settings for dig_author project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = '$a9%)yu7a599ez7ot+s9dssk)(+5s^s#sw(oiqg_fi3wk!j0s7'
=======
SECRET_KEY = ''
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '*.photoword.net']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'digs',
    'show_author',
<<<<<<< HEAD
    # start zinnia
    'django.contrib.sites',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
    # end zinnia
=======
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dig_author.urls'

WSGI_APPLICATION = 'dig_author.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/STATIC/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Customizing project's templates
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

<<<<<<< HEAD
SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

EMAIL_HOST = "smtp.qq.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_HOST_USER = "1258080923@qq.com"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
=======
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02
