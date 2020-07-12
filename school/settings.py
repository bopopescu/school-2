"""
Django settings for tutorial project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import djcelery
import datetime
from . import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY
### qq小程序秘钥
QQ_SECRET = config.QQ_SECRET
wx_SECRET = config.wx_SECRET
### QQ 小程序APPID
QQ_APPID = '1110027966'
wx_APPID = 'wxef282571c30a328e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.ENV_CONFIG[config.CURRENT_ENV]["DEBUG"]

ALLOWED_HOSTS = ['*']

# cookie超时时间，最好是永远 ^_^ !
SESSION_COOKIE_AGE = 60*60*600000
SESSION_SAVE_EVERY_REQUEST = True

# 用redis做缓存配置

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1,
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
            # "CLIENT_CLASS": "django_redis.client.HerdClient",
            # "PARSER_CLASS": "redis.connection.HiredisParser"
        },
    },
    'sessions': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1,
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
            # "CLIENT_CLASS": "django_redis.client.HerdClient",
            # "PARSER_CLASS": "redis.connection.HiredisParser"
        },
    },
}

# 爬虫设置
# 默认IP每秒最大访问频率
MAX_IP_FREQUENT = 10
# 默认封禁IP时间 5 秒
BLOCK_IP_TIME = 5

# DRF关于缓存的拓展
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

REDIS_TIMEOUT = 7*24*60*60
CUBES_REDIS_TIMEOUT = 60*60
NEVER_REDIS_TIMEOUT = 365*24*60*60

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    # 'snippets',
    'yonghu',
    'djcelery',
    'forum',
    'transaction',
    'readAndReplyNumAndLikes',
    'Messages',
    'images',
    'feedback',
]

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAdminUser',
#     ],
#     'PAGE_SIZE': 10
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middlewares.antiSpiders.AntiSpider', # 反爬中间件
]

ROOT_URLCONF = 'school.urls'

# jwt接口验证
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_ALLOW_REFRESH':True
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



# Mysql数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.ENV_CONFIG[config.CURRENT_ENV]["MYSQL_DATABASE_NAME"],
        'USER': config.MYSQL_USER,
        'PASSWORD': config.MYSQL_PASSWORD,
        'HOST': config.MYSQL_HOST,
        'PORT': config.MYSQL_PORT
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'yonghu.views.MyYonghuBackend',
    "django.contrib.auth.backends.ModelBackend"
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    # 配置默认的认证方式 base:账号密码验证
    #session：session_id认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # drf的这一阶段主要是做验证,middleware的auth主要是设置session和user到request对象
        # 默认的验证是按照验证列表从上到下的验证
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Internationalization-
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

### 系统邮件发送配置 ###
# DOMAIN = 'http://127.0.0.1:3389/auth' #用户验证邮箱访问地址
# 设置邮件域名
EMAIL_HOST = "smtp.exmail.qq.com"
# 设置端口号
EMAIL_PORT = 465
# 发件人邮箱
EMAIL_HOST_USER = 'gaojunbin@gaoblog.cn'
# 发件人姓名
EMAIL_WEBITE_NAME = '超级管理员'
# 发件人授权码
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
# 设置是否启用安全链接
EMAIL_USE_SSL = True
#是否使用TLS安全传输协议
EMAIL_USE_TLS = False

ERROR_FROM = 'gaojunbin@gaoblog.cn'

#搜索
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.article.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

### Celery配置
# celery回去查看INSTALLD_APP下查看每个app下面的目录中的tasks.py文件，找到标记为task的方法，将它们注册为celery task
djcelery.setup_loader()
# broker的代理地址
BROKER_URL = config.BROKER_URL
#celery结果返回，可用于跟踪结果
CELERY_RESULT_BACKEND = config.CELERY_RESULT_BACKEND
# tasks.py文件所在位置
CELERY_IMPORTS = ('school.tasks', )
#celery时区设置，使用settings中TIME_ZONE同样的时区
CELERY_TIMEZONE = TIME_ZONE
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# 每个worker执行了多少任务就会销毁，防止内存泄露，默认是无限的
CELERYD_MAX_TASKS_PER_CHILD = 5
# 设置并发的worker数量
CELERYD_CONCURRENCY = 4
# 有些情况可以防止死锁
CELERY_FORCE_EXECV = True
CELERY_ENABLE_UTC = True

# 下面是定时任务的设置，我一共配置了三个定时任务.
# from celery.schedules import crontab
# CELERYBEAT_SCHEDULE = {
#     '每小时获取数据': {
#         "task": "yonghu.tasks.getApi",
#         #"schedule": crontab(minute='*/3',),
#         "schedule": crontab(0,'*','*','*','*'),
#         "args": (),
#     },
#     '每周一进行数据库清理': {
#         'task': 'yonghu.tasks.removeApi',
#         'schedule': crontab(hour='*/9', minute='*/50', day_of_week='*/5'),
#         "args": ()
#     },
#     '每天进行数据库备份': {
#         'task': 'yonghu.tasks.backups',
#         'schedule': crontab(0,1,'*','*','*'),
#         "args": ()
#     },
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]