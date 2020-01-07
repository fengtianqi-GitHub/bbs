#用户管理视图
from flask import Blueprint

user = Blueprint('user',__name__,url_prefix='/user')
@user.route('/')
def index():
    return '用户管理'
