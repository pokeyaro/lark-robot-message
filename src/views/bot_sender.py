# -*- coding: UTF-8 -*-
import json
from flask import Blueprint
from flask import Response, request, abort
from api.lark import send
from configs.settings import SERVE


# 实例化蓝图对象
bp = Blueprint('msg', __name__)


# 业务视图函数
@bp.route(rule=SERVE.API.ROBOT_MSG, methods=['POST'], endpoint='msg')
def message():
    # 判断token
    access_token = request.headers.get('Authorization')
    if access_token != f"Token {SERVE.ENV.SELF_AUTH_TOKEN}":
        # HTTP 403 Forbidden.
        abort(403)

    # 判断请求方法
    if (request.method != 'POST'):
        # HTTP 405 Method Not Allowed.
        abort(405)

    # 获取POST请求数据
    email = request.json.get("email")
    title = request.json.get("title")
    content = request.json.get("content")

    # 如果email为空
    if email is None:
        # HTTP 422 Unprocessable entity.
        data = json.dumps({
            'code': 422,
            'msg': 'Request missing required parameter',
            'data': {}
        })
        return Response(data, status=422, content_type='application/json')

    # 获取请求体
    params = {
        'email': email,
        'title': title,
        'content': content
    }

    # 发送请求成功
    send(**params)
    data = json.dumps({
        'code': 0,
        'msg': 'success',
        'data': params
    })
    return Response(data, status=200, content_type='application/json')
