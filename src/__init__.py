# -*- coding: UTF-8 -*-
from flask import Flask
from .views.bot_sender import bp
from configs.settings import SERVE

def create_app():
    # 实例化Flask对象
    app = Flask(__name__)

    # 注册一个蓝图
    app.register_blueprint(blueprint=bp, url_prefix=SERVE.API.BASE)

    # 返回对象
    return app
