from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# --------------------------------------------------
# Base Directory
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# Load Environment Variables
load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------
# Security
# --------------------------------------------------

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "test-secret-key"
)

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "*"
).split(",")

# --------------------------------------------------
# Applications
# --------------------------------------------------

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    'rest_framework',
    'corsheaders',

    # Local Apps
    'accounts',
    'skills',
    'exchange',
    'reviews',
    'community',
    'ai_features',
]

# --------------------------------------------------
# Middleware
# --------------------------------------------------

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------
# URLs / WSGI
# --------------------------------------------------

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# --------------------------------------------------
# Templates
# --------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --------------------------------------------------
# Database (Neon PostgreSQL)
# --------------------------------------------------



# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3",
        conn_max_age=600
    )
}

# --------------------------------------------------
# Password Validation
# --------------------------------------------------

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

# --------------------------------------------------
# Internationalization
# --------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# --------------------------------------------------
# Static Files
# --------------------------------------------------

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --------------------------------------------------
# Default Primary Key
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------
# DRF
# --------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# --------------------------------------------------
# CORS
# --------------------------------------------------

CORS_ALLOW_ALL_ORIGINS = True

# --------------------------------------------------
# Custom User Model
# --------------------------------------------------

AUTH_USER_MODEL = 'accounts.User'

# --------------------------------------------------
# Gemini AI
# --------------------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")