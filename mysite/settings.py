from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ["friendbook.api.codewithjoe.in", '13.203.74.24', 'friendbook.codewithjoe.in', "*"]
AUTH_USER_MODEL = 'UserManagement.User'

INSTALLED_APPS = [
    "corsheaders",
    "daphne",
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # External Apps
    'rest_framework_simplejwt',
    'rest_framework',
    'django_celery_beat',
    "storages",

    # Internal Apps
    'UserManagement',
    "Profiles",
    "AdminPanel",
    'ReportApp',
    "Chat",
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'mysite.urls'

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


CSRF_TRUSTED_ORIGINS = [
    "https://friendbook.api.codewithjoe.in"
]


AUTHENTICATION_BACKENDS = [
    'UserManagement.custom_authenticate.EmailorUsernameValidate',
    'django.contrib.auth.backends.ModelBackend',
]

WSGI_APPLICATION = 'mysite.wsgi.application'
ASGI_APPLICATION = 'mysite.asgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'friendbook',
        'USER': 'postgres',
        'PASSWORD': 'Sneha@1103',
        'HOST': 'friendbook.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

DATASET_DIR = os.path.join(BASE_DIR , 'data')

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Azure storage settings
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME', 'friendbookstorage')
AZURE_STATIC_CONTAINER = 'static'
AZURE_MEDIA_CONTAINER = 'media'
AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')

AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"

# Media files configuration
DEFAULT_FILE_STORAGE = 'mysite.storage_backends.CustomAzureMediaStorage'
MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/"

# Static files configuration
STATICFILES_STORAGE = 'mysite.storage_backends.CustomAzureStaticStorage'
STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/"




CELERY_BROKER_URL = "redis://redis:6379/0"  # Redis database 0 is used for the broker.
CELERY_RESULT_BACKEND = "redis://redis:6379/1"  # Redis database 1 is used for storing task results.

CELERY_ACCEPT_CONTENT = ['json']  # Accept only JSON serialized content.
CELERY_TASK_SERIALIZER = 'json'  # Use JSON for serializing tasks.
CELERY_RESULT_SERIALIZER = 'json'  # Use JSON for serializing results.
CELERY_TIMEZONE = 'UTC'  # Set UTC as the timezone.

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': ["redis://redis:6379/0"],  # Correct Redis host configuration.
        },
    },
}



SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'codewithjoe16@gmail.com'
EMAIL_HOST_PASSWORD = 'uhwj zzog jevi qryv'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
