import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    #heroku = 'postgresql://aumimjzwyzqhne:a0a5b96b45403b4ed5439b00de9a900ac1f605d70cd3e6721fe7c79d5c61a3dd@ec2-54-173-138-144.compute-1.amazonaws.com:5432/d9ekdi36m71bi3'
    #localhost = 'mysql+pymysql://root:@localhost/driving-school'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = 'postgresql://aumimjzwyzqhne:a0a5b96b45403b4ed5439b00de9a900ac1f605d70cd3e6721fe7c79d5c61a3dd@ec2-54-173-138-144.compute-1.amazonaws.com:5432/d9ekdi36m71bi3'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    #python_anywhere = 'mysql+pymysql://anurajsinngh:drivingschool@anurajsinngh.mysql.pythonanywhere-services.com/anurajsinngh$Driving_School'
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

def version(path, version=1):
    return f"/v{version}/{path}"
