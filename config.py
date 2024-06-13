import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cuongnh20storage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'JSNSMSONlvTKttkU7sF49jqiZGxCuM3/+eaQwALwPQVEPx0ejoI+GQBiE7MTcz2kd1Q71dN8rFrY+AStVFe0ww=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cuongnh20.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cuongnh20_db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cuongnh20'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Sql@02071708'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{SQL_USER_NAME}:{quote_plus(SQL_PASSWORD)}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "4Zi8Q~SZ0NFj9v~z6xgSZ5dLQkSwyEEXJtK4xaL5"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "50bcfa10-b475-49cf-a3e7-9fea4d22e1f9"

    REDIRECT_PATH = "/get_a_token"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session