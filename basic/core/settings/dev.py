import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@!u!t(b1t@c@*ot8w@j9vxx)$-vr!kdnk@y@c9p0)3ly06!c4d'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', True)
DEBUG = False # keep it false, so it won't give internal exceptions of django

ALLOWED_HOSTS = [
    "localhost",
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler", 
            "formatter": "simple-console"
        },
        # "all_files": {
        #     "level": "INFO",
            # "class": "logging.FileHandler",
            # "filename": "./news_be/logs/all_files.log",
        #     "formatter": "verbose-file",
        # },
    },
    "loggers": {
        # "django": {
        #     "handlers": ["all_files"],
        #     "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        #     "propagete": True,
        # },
        'django.utils.autoreload': {
            'level': 'CRITICAL',
        },
        # "news_api": {
        #     "handlers": ["all_files"],
        #     "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        #     "propagete": True,
        # },
        # "common": {
        #     "handlers": ["all_files"],
        #     "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        #     "propagete": True,
        # },
        # "exceptions":{
        #     "handlers": ["all_files"],
        #     "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        #     "propagete": True,
        # },
        "root": {"handlers": ["console"], "level": "WARNING"},
    },
    "formatters": {
        "verbose-file": {
            "format": "[{levelname}] [{asctime}] [L{lineno}] [FILE:{filename}] [FUNC:{funcName}] [{name}] - {message}",
            "style": "{",
        },
        "basic": {
            "format": "[{levelname}] [{name}]  [L:{lineno}] {message}",
            "style": "{",
        },
        "simple-console": {
            "format": "[{levelname}] [L{lineno}] [FILE:{filename}] [{name}] - {message}",
            "style": "{",
        },
    },
}