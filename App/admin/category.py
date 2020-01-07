#板块管理
from flask import Blueprint

category = Blueprint('category',__name__,url_prefix='/admin')

@category.route('/category')
def index():
    return '板块管理'
