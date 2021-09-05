from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        # 'Trusted_Connection': 'yes',
        # 'HOST':'localhost\\SQLEXPRESS',
        # 'OPTIONS':{
        #     'driver': 'SQL Server Native Client 11.0', 
        # }
    }
}



# 'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'BDChacuntados',
#         'Trusted_Connection': 'yes',
#         'HOST':'localhost\\SQLEXPRESS',
#         'OPTIONS':{
#             'driver': 'SQL Server Native Client 11.0', 
#         }
#     }