#前端视图
from flask import Blueprint

bbs = Blueprint('bbs',__name__)

@bbs.route('/')
def index():
    return '首页'
