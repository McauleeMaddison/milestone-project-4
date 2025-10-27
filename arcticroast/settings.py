from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# === Installed Apps ===
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'apps.dashboard',
    'apps.products',
    'apps.payments',
]

# === Templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # global template folder
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

# === Static & Media ===
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']       # where you author files
STATIC_ROOT = BASE_DIR / 'staticfiles'         # where collectstatic stores them

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
