DEBUG = True

USERNAME = 'root'
PASSWORD = 'vitor1230'
SERVER = 'localhost'
DB = 'flask_fundamentos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "minha_chave_secreta"

BABEL_DEFAULT_LOCALE = 'pt'
