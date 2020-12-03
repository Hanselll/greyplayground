from flask import Flask
#from app.models.book import db#
from flask_login import LoginManager#介个东东提供了现成的cookie
from flask_mail import Mail

login_manager = LoginManager()#实例化
mail = Mail()

def create_app():
    app = Flask(__name__)
    #app.config.from_object('app.secure')
    #app.config.from_object('app.settings')
    register_bp(app)

    #db.init_app(app)#
    #with app.app_context():
        #db.create_all()

    #login_manager.init_app(app)#初始化login_manager
    #login_manager.login_view = 'web.login'#告诉flask一个默认的登录视图函数
    #login_manager.login_message = '请先登录'
    #mail.init_app(app)

    return app

def register_bp(a):
    from app.web import web
    a.register_blueprint(web)