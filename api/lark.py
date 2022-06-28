# -*- coding: UTF-8 -*-
import json
import requests
import functools
from configs.settings import *


# 飞书认证装饰器
def lark_auth(func):
    """
    Get token access to Feishu app (valid for 2 hours).
    """
    @functools.wraps(func)
    def get_app_access_token(email, fmtData):
        url = LARK.URL.ACCESS_TOKEN
        payload = json.dumps({
            "app_id": LARK.ENV.APP_ID,
            "app_secret": LARK.ENV.APP_SECRET,
        })
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Proxy-Authorization": f"Bearer {LARK.ENV.TOKEN_AUTH}"
        }
        response = requests.request(
            method="POST",
            url=url,
            headers=headers,
            data=payload,
        )
        token = ""
        if response.status_code == 200:
            token = response.json().get("tenant_access_token")
        return func(email, fmtData, token)
    return get_app_access_token


# 发送消息卡片的API
@lark_auth
def _send_msg_card(email: str, fmtData: str, token: str) -> str:
    """
    Send message card.
    """
    url = LARK.URL.SEND_MSG
    payload = json.dumps({
        "receive_id": email,
        "content": fmtData,
        "msg_type": "interactive"
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        data=payload,
    )
    if response.status_code == 200:
        msg = response.json().get("msg")
        return msg
    return ""


# 发送消息函数
def send(email: str = None, title: str = None, content: str = None) -> str:
    from cards.base import BOT
    bot = BOT()
    bot.INPUT(receiver=email, theme=title, body=content)
    format_data = bot.OUTPUT
    res = _send_msg_card(email=email, fmtData=format_data)
    return res
