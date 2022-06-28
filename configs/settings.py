# -*- coding: UTF-8 -*-
import os


class PATH:
    """
    项目文件/路径相关
    """
    ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    JSON: str = os.path.join(ROOT, "cards/types/basic.json")


class LARK:
    """
    飞书API相关
    """
    class ENV:
        APP_ID: str = os.getenv("LARK_APP_ID")
        APP_SECRET: str = os.getenv("LARK_APP_SECRET")
        TOKEN_AUTH: str = os.getenv("LARK_AUTH_BEARER")

    class URL:
        ACCESS_TOKEN: str = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal"
        SEND_MSG: str = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=email"


class SERVE:
    """
    服务本身相关
    """
    class ENV:
        SELF_AUTH_TOKEN: str = os.getenv("SELF_AUTH_TOKEN")

    class CONN:
        HOST: str = '0.0.0.0'
        PORT: int = 8000

    class API:
        BASE: str = "/api"
        ROBOT_MSG: str = "/robot-msg"


