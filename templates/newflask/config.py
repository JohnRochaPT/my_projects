''' Configuration file '''
#; 'DEBUG': False, 
#; 'TESTING': False,
#; 'PROPAGATE_EXCEPTIONS': None, 
#; 'SECRET_KEY': None, 
#; 'SECRET_KEY_FALLBACKS': None, 
#; 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 
#; 'USE_X_SENDFILE': False, 
#; 'TRUSTED_HOSTS': None, 
#; 'SERVER_NAME': None, 
#; 'APPLICATION_ROOT': '/', 
#; 'SESSION_COOKIE_NAME': 'session', 
#; 'SESSION_COOKIE_DOMAIN': None, 
#; 'SESSION_COOKIE_PATH': None, 
#; 'SESSION_COOKIE_HTTPONLY': True, 
#; 'SESSION_COOKIE_SECURE': False, 
#; 'SESSION_COOKIE_PARTITIONED': False, 
#; 'SESSION_COOKIE_SAMESITE': None, 
#; 'SESSION_REFRESH_EACH_REQUEST': True, 
#; 'MAX_CONTENT_LENGTH': None, 
#; 'MAX_FORM_MEMORY_SIZE': 500000, 
#; 'MAX_FORM_PARTS': 1000, 
#; 'SEND_FILE_MAX_AGE_DEFAULT': None, 
#; 'TRAP_BAD_REQUEST_ERRORS': None, 
#; 'TRAP_HTTP_EXCEPTIONS': False, 
#; 'EXPLAIN_TEMPLATE_LOADING': False, 
#; 'PREFERRED_URL_SCHEME': 'http', 
#; 'TEMPLATES_AUTO_RELOAD': None, 
#; 'MAX_COOKIE_SIZE': 4093, 
#; 'PROVIDE_AUTOMATIC_OPTIONS': True}

#: Main class
class Config(object):
    SECRET_KEY = 'K5QwCWsJ8qkypg2R3rifHnI0O7'
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'

#: Production systems WITH NO database or email functionality
class ConfigProdNoDbNoMail(Config):
    DEBUG = False
    TESTING = False

#: Production systems WITH database and email functionality
class ConfigProdWithDBWithMail(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod_surveys.db'
    MAIL_SERVER = 'mail.smartshots.org'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'noreply@smartshots.org'
    MAIL_PASSWORD = '#Pfd7*x8kp3H&B'


#: Development systems WITH NO database or email functionality
class ConfigDevNoDbNoMail(Config):
    DEBUG = True
    TESTING = True

#: Development systems WITH database and email functionality
class ConfigDevWithDBWithMail(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_surveys.db'
    MAIL_SERVER = 'mail.smartshots.org'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'noreply@smartshots.org'
    MAIL_PASSWORD = '#Pfd7*x8kp3H&B'
