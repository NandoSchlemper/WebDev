import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'henrique_lindo_<3' # Se a Secret Key nao for definida, setar essa
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db' # Se o DB nao for definido, setar esse como default
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Nao faz o tracking das modificacoes, deixando mais leve ;)
