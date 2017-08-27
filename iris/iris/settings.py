"""
Django settings for iris project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^8xxu^ycbqg-=xjx+jn3e^830y+_)-xi-sf4l5&)2hqacd*k7l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    # 'modeltranslation',
    'suit',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'smart_selects',
    'localflavor',
    'sorl.thumbnail',
    'report_builder',
    'bootstrap3',
    'django_extensions',
    'import_export',
    # My apps
    'location',
    'commons',
    'people',
    'employees',
    'housing',
    'members',
    'suppliers',
    'doctors',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'iris.urls'
#
# TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#     'django.core.context_processors.request',
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.core.context_processors.request',
                'django.template.context_processors.request',
                # 'django.core.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'iris.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

# gettext = lambda s:
# LANGUAGES = (
#     ('es', gettext('Spanish')),
#     ('en', gettext('English')),
# )
#
#
# MODELTRANSLATION_TRANSLATION_FILES = (
#     'members.translation',
#     # 'employees.translation',
# )

TIME_ZONE = 'America/Santo_Domingo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(
    os.path.dirname(BASE_DIR),
    "static_in_env", "static_root"
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    os.path.join(BASE_DIR, "static_in_env"),
    # '/var/www/static/',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

USE_DJANGO_JQUERY = False

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Iris ACICIRD',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'SEARCH_URL': '/admin/members/member/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'commons': 'icon-random',
        'doctors': 'icon-calendar',
        'employees': 'icon-user',
        'housing': 'icon-home',
        'location': 'icon-map-marker',
        'members': 'icon-eye-close',
        'people': 'icon-user',
        'suppliers': 'icon-briefcase',
    },
    'MENU_OPEN_FIRST_CHILD': False,  # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    # 'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    # {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}
