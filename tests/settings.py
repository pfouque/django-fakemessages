from __future__ import annotations

from os import path

DEBUG = True
TEMPLATE_DEBUG = True
USE_TZ = True

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "test.db"}}

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fakemessages",
)

MIDDLEWARE = [
    # default django middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

PROJECT_DIR = path.abspath(path.join(path.dirname(__file__)))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
            ]
        },
    }
]

STATIC_URL = "/static/"

SECRET_KEY = "secret"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s %(message)s"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {
        "": {"handlers": ["console"], "propagate": True, "level": "DEBUG"},
        # 'django': {
        #     'handlers': ['console'],
        #     'propagate': True,
        #     'level': 'WARNING',
        # },
    },
}

ROOT_URLCONF = "tests.urls"

if not DEBUG:
    raise Exception("This settings file can only be used with DEBUG=True")

LANGUAGE_CODE = "en"
LANGUAGES = [
    ("fr", "Français"),
    ("en", "English"),
    ("de", "Deutsch"),
]

if DEBUG:
    from django.conf.locale import LANG_INFO

    FAKE_LANGUAGE_CODE = "▮▮"

    LANG_INFO[FAKE_LANGUAGE_CODE] = {
        "bidi": False,
        "code": FAKE_LANGUAGE_CODE,
        "name": "▮▮▮▮▮▮▮▮",
        "name_local": "🖖 ▮▮▮▮▮▮▮",
    }
    LANGUAGES.append((FAKE_LANGUAGE_CODE, "🖖 ▮▮▮▮▮▮▮"))
