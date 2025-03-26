"""
Django settings for NSNFRONTBACK project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(c8o^r6kufs3miybg0=#@1(_ag&tmklzjz*nc+&jk&#m5&9_e8'
# lynx-many-informally.ngrok-free.app
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Your specific IP address
LOCAL_IP = '192.168.84.106'
ngrok=  'lynx-many-informally.ngrok-free.app'
# Allow connections from all local network devices
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', LOCAL_IP,ngrok]


# Application definition

INSTALLED_APPS = [
    'admin_interface', # only if django version < 1.9 
    'colorfield', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'silk',
    'import_export',
    'authnsn',
    'staffnsn',
    'studentnsn',
    'activities',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Make sure this is before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'silk.middleware.SilkyMiddleware',
]

ROOT_URLCONF = 'NSNFRONTBACK.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'NSNFRONTBACK.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL
        'NAME': 'dbnsn1',
        'USER': 'root',
        'PASSWORD': 'Veera12',
        'HOST': '127.0.0.1',  # Or 'localhost' for local MySQL
        'PORT': '3306',  # Default MySQL port
    }
}

# CORS settings for local development
CORS_ALLOW_ALL_ORIGINS = True  # For development only
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    f"http://{LOCAL_IP}:8000",
    f"https://{ngrok}",
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    f'http://{LOCAL_IP}:8000',
    f"https://{ngrok}",
]

HTMX_CSRF_COOKIE_NAME = 'csrftoken'

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_COOKIE': 'access',
    'AUTH_COOKIE_SECURE': False,  # Set to False for local network development
    'AUTH_COOKIE_HTTP_ONLY': True,
    'AUTH_COOKIE_PATH': '/',
    'AUTH_COOKIE_SAMESITE': 'Lax',  # Changed from 'Strict' for local development
}

# Cookie settings for local development
SESSION_COOKIE_SECURE = False  # Set to False for HTTP in local development
CSRF_COOKIE_SECURE = False  # Set to False for HTTP in local development
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Changed from 'Strict' for local development
CSRF_COOKIE_SAMESITE = 'Lax'  # Changed from 'Strict' for local development

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'login': '3/day',  # Limits to 3 login attempts per day
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
    }
}

# Custom Authentication Backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'authnsn/static'),
    # or if authnsn is your app name:
    # os.path.join(BASE_DIR, 'authnsn', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# For development
MAX_UPLOAD_SIZE = 10 * 1024 * 1024

# Allowed file types
ALLOWED_DOCUMENT_TYPES = [
    'image/jpeg',
    'image/png',
    'application/pdf'
]
X_FRAME_OPTIONS='SAMEORIGIN' 