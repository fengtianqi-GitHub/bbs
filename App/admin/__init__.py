from .category import category

def dog_blueprint(app):
    app.register_blueprint(category)