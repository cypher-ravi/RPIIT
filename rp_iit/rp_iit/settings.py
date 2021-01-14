"""
Django settings for rp_iit project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# for heroku
# import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#0qw1@n7rpu1#-9+hak=nzk8l0@%anqiz@5cli2ax9utqi&y8g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'rest_api',
    'Payment_gateway',
    

    #third party libraries
    'rest_framework',
    'drf_extra_fields',
    'rest_framework_swagger',
    'drf_yasg',
    
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'rp_iit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rp_iit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ddm391ps95d268',
#         'USER': 'bmepsvklzyxonk',
#         'PASSWORD':'5661d1535b3a06fdc270641c8abd67e47a518030422f6bc7664418ef6bb43950',
#         'HOST': 'ec2-18-235-107-171.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
    'OPTIONS': {'use_pure': True }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
from django.utils import timezone

# my_local_time = timezone.localtime(timezone.now())
TIME_ZONE =  'GMT'


USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
VENV_PATH = os.path.join(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(VENV_PATH, 'media')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        # 'rest_framework.permissions.IsAuthenticated',
        
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

AUTH_USER_MODEL = "authentication.User"




SWAGGER_SETTINGS = {
    'LOGIN_URL': 'A5740DB2B7C1FE79CA9A2FDC8491B2C6/auth/login',
    'LOGOUT_URL': 'A5740DB2B7C1FE79CA9A2FDC8491B2C6/auth/logout/',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SHOW_REQUEST_HEADERS': True
}

# django_heroku.settings(locals())
    
FCM_SERVER_KEY="[AAAAcJkoZ-I:APA91bE2NWUD-Q5O5MB8gQaLnN9cQ72hw3T_micRtdO1qPb6qSzGDJhx3iyVJyKqOTsuQujwVt04zG2MPunMmkARVTERoPVGgSI47RSCnBBSwkAZRIzim1xrbvO00Dl3oHeLjnIqTQ_q]"



PAYU_CONFIG = {
        "merchant_key": "ZQGI2x56",
        "merchant_salt": "VTsYoY3kBp",
        "mode": "test",
        "success_url": "http://127.0.0.1:8000/payment/success",
        "failure_url": "http://127.0.0.1:8000/payment/failure"
  }