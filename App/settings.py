#配置文件
class BaseConfig:
    DEBUG = False
    SECRET_KEY = 'ae3856f5-df00-4cda-a963-3c2141524d12'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/py2020"

class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/py2020"

config = {
    'default':BaseConfig,
    'develop':DevelopConfig,
    'product':ProductConfig
}