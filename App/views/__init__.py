#前端和用户蓝图注册
from .user import user
from .views import bbs


def cat_blueprint(app):
    app.register_blueprint(user)
    app.register_blueprint(bbs)