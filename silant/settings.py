from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-change-this-key"


DEBUG = True


ALLOWED_HOSTS = []



# -----------------------------------------------------------------------------
# Приложения
# -----------------------------------------------------------------------------

INSTALLED_APPS = [

    # Django

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",


    # Third-party

    "rest_framework",
    "django_filters",

    "allauth",
    "allauth.account",


    # Apps

    "accounts",
    "core",
    "references",
    "machines",
    "maintenance",
    "complaints",
    "api",

]


SITE_ID = 1



# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]



# -----------------------------------------------------------------------------
# URLs
# -----------------------------------------------------------------------------

ROOT_URLCONF = "silant.urls"




# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------

TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]



WSGI_APPLICATION = "silant.wsgi.application"




# -----------------------------------------------------------------------------
# Database
# -----------------------------------------------------------------------------

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",

    }

}




# -----------------------------------------------------------------------------
# Password validation
# -----------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]




# -----------------------------------------------------------------------------
# Internationalization
# -----------------------------------------------------------------------------

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Minsk"

USE_I18N = True

USE_TZ = True





# -----------------------------------------------------------------------------
# Static / Media
# -----------------------------------------------------------------------------

STATIC_URL = "static/"


STATICFILES_DIRS = [

    BASE_DIR / "static",

]


STATIC_ROOT = BASE_DIR / "staticfiles"



MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media"





# -----------------------------------------------------------------------------
# Default PK
# -----------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"





# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------

LOGIN_URL = "/accounts/login/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"





# -----------------------------------------------------------------------------
# Authentication
# -----------------------------------------------------------------------------

AUTHENTICATION_BACKENDS = [

    "django.contrib.auth.backends.ModelBackend",

    "allauth.account.auth_backends.AuthenticationBackend",

]





# -----------------------------------------------------------------------------
# django-allauth
# -----------------------------------------------------------------------------

ACCOUNT_LOGIN_METHODS = {
    "username"
}


ACCOUNT_SIGNUP_FIELDS = [

    "username*",

    "password1*",

    "password2*",

]


ACCOUNT_EMAIL_VERIFICATION = "none"



# ВАЖНО:
# Пользователи создаются только администратором через Django Admin.
# Самостоятельная регистрация отключена.

ACCOUNT_ALLOW_SIGNUPS = False



ACCOUNT_ADAPTER = "accounts.adapters.AccountAdapter"





# -----------------------------------------------------------------------------
# Django REST Framework
# -----------------------------------------------------------------------------

REST_FRAMEWORK = {

    "DEFAULT_FILTER_BACKENDS": [

        "django_filters.rest_framework.DjangoFilterBackend",

    ],

}