from .base import*

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','0.0.0.0']

#the default DB setting
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #   }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wasisi',
        'USER': 'wasisiAdmin',
        'PASSWORD': 'letmein',
        'HOST': 'localhost',
        'PORT': '',
        # #Adding following 2 lines because of Foreign Key issues. https://docs.djangoproject.com/en/dev/ref/databases/
        'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    }
    }
}

# Add redis hosts. This is done after pip install redis==2.10.3, python manage.py shell, >>>import redis, >>>r = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0