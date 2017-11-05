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
    }
}