from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "versatileimagefield",
    "tinymce",
    "crispy_forms",
    "crispy_bootstrap5",
    "import_export",
    "registration",
    "widget_tweaks",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "user_sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "web",
    "invoices",
    "services",
    "accounts",
    "notification",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "user_sessions.middleware.SessionMiddleware",
    # "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
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
            ],
            "libraries": {"custom_tags": "web.templatetags.custom_tags"},
        },
    }
]

WSGI_APPLICATION = "usklogin.wsgi.application"
ASGI_APPLICATION = "usklogin.asgi.application"

DATABASES = {
    "default": {"ENGINE": config("DB_ENGINE"), "NAME": config("DB_NAME"), "USER": config("DB_USER"), "PASSWORD": config("DB_PASSWORD"), "HOST": config("DB_HOST"), "PORT": ""}
}

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

SILENCED_SYSTEM_CHECKS = ["admin.E410"]


USE_L10N = False
DATE_INPUT_FORMATS = ("%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y", "%d %b %Y", "%d %b, %Y", "%d %b %Y", "%d %b, %Y", "%d %B, %Y", "%d %B %Y")
DATETIME_INPUT_FORMATS = ("%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y", "%d/%m/%y %H:%M:%S", "%d/%m/%y %H:%M", "%d/%m/%y", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d")

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"

AUTH_USER_MODEL = "accounts.User"
DOMAIN = "https://usklogin.geany.website"
# DOMAIN = "http://127.0.0.1:8000"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SESSION-ENGINE FOR CUSTOM SESSESIOM
SESSION_ENGINE = "user_sessions.backends.db"
MAX_DEVICE_SESSIONS = 3

# Registration REDUX
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False
SEND_ACTIVATION_EMAIL = False
REGISTRATION_EMAIL_SUBJECT_PREFIX = ""

REGISTRATION_OPEN = True
LOGIN_URL = "/start/"
LOGOUT_URL = "app/logout/"
LOGIN_REDIRECT_URL = "/"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp-relay.sendinblue.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "loginusk@gmail.com"
EMAIL_HOST_PASSWORD = "D2ja7rJgAnQFTS5Z"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

MAILGUN_FROM_EMAIL = "secure.gedexo@gmail.com"


# For development
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
# CSRF_TRUSTED_ORIGINS = ["https://pvanfas-humble-computing-machine-5x49x4p74vj2vrj5-8000.preview.app.github.dev"]
