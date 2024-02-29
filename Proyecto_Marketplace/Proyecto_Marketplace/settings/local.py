from .base import *
import ibm_db_django

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'tiendavirtual',
        'USER'     : '90308578',
        'PASSWORD' : 'AF4E0E621EEEA652A43A6DBDA92A7242666A575C7AD0EAB803D4A9678FEDD393',
        'HOST'     : '10.44.1.159',
        'PORT'     : '5432',
        #'PCONNECT' :  True, 
    },
    'DB2_Authoring':{
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