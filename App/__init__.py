from flask import Flask
from App.extensions import init_app
from App.settings import config
from App.views import cat_blueprint
from App.admin import dog_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.get('develop','default'))
    init_app(app)
    dog_blueprint(app)
    cat_blueprint(app)
    return app