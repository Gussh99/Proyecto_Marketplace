from .base import *
import ibm_db_django

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'ibm_db_django',
        'NAME':'coppeldb',
        'USER'     : 'ecomm',
        'PASSWORD' : 'Cop1Db2',
        'HOST'     : '10.62.10.83',
        'PORT'     : '50005',
        'PCONNECT' :  True, 
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'