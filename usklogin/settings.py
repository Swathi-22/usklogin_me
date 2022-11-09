from errno import EMLINK
from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    # 3rd party packages
    "user_sessions",
    "channels",
    "django_celery_beat",
    "django_celery_results",
    "crispy_forms",
    "crispy_bootstrap5",
    "versatileimagefield",
    "tinymce",
    "import_export",
    #
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # apps
    "web",
    "invoices",
    "services",
    "notification",
    "accounts",
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "user_sessions.middleware.SessionMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "usklogin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "web.context_proccessor.notifications",
                "web.context_proccessor.main_context",
            ]
        },
    }
]

WSGI_APPLICATION = "usklogin.wsgi.application"
ASGI_APPLICATION = "usklogin.asgi.application"


# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE'),
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': '',
#     }
# }


DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


VERSATILEIMAGEFIELD_SETTINGS = {
    "cache_length": 2592000,
    "cache_name": "versatileimagefield_cache",
    "jpeg_resize_quality": 70,
    "sized_directory_name": "__sized__",
    "filtered_directory_name": "__filtered__",
    "placeholder_directory_name": "__placeholder__",
    "create_images_on_demand": True,
    "image_key_post_processor": None,
    "progressive_jpeg": False,
}


LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True


USE_L10N = False
DATE_INPUT_FORMATS = ("%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y", "%d %b %Y", "%d %b, %Y", "%d %b %Y", "%d %b, %Y", "%d %B, %Y", "%d %B %Y")
DATETIME_INPUT_FORMATS = ("%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y", "%d/%m/%y %H:%M:%S", "%d/%m/%y %H:%M", "%d/%m/%y", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d")

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CHANNEL_LAYERS = {"default": {"BACKEND": "channels_redis.core.RedisChannelLayer", "CONFIG": {"hosts": [("127.0.0.1", 6379)]}}}

# DJANGO-SESSION
SESSION_ENGINE = "user_sessions.backends.db"
MAX_DEVICE_SESSIONS = 3

# CELERY SETTINGS

CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SELERLIZER = "json"
CELERY_TIMEZONE = "Asia/Kolkata"

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# EMAIL SETTINGS

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "mkswathisuresh@gmail.com"
EMAIL_HOST_PASSWORD = "rrkimjacfiuwqcic"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# user model created
AUTH_USER_MODEL = "accounts.User"
