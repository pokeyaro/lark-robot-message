# -*- coding: UTF-8 -*-
import os
import json
import typing as t
from configs.settings import PATH


# json格式注解标记
JSONType = t.Union[str, int, float, bool, None, t.Dict[str, t.Any], t.List[t.Any]]


class BOT(object):
    """
    输入/输出详细卡片
    """
    _card: str = PATH.JSON

    def __init__(self) -> None:
        if os.path.exists(self._card) and os.path.isfile(self._card):
            with open(self._card, mode='rt', encoding='utf-8') as j:
                self._contents = json.loads(j.read())
        else:
            raise FileNotFoundError(f"open: {self._card}: No such file or directory.")

    def _update(self) -> None:
        # 格式化替换内容
        try:
            # theme
            self._contents["header"]["title"]["content"] = self._contents["header"] \
                ["title"]["content"].replace("Theme", self.theme)
            # body
            self._contents["elements"][0]["content"] = self._contents["elements"][0] \
                ["content"].replace("Email", self.receiver).replace("Content", self.body)
        except Exception as e:
            raise Exception(e)

    def INPUT(self, receiver=None, theme=None, body=None) -> None:
        if receiver is None:
            raise TypeError("Receiver cannot be empty.")
        elif isinstance(receiver, str):
            self.receiver = receiver
        else:
            raise TypeError("Receiver must be an string.")

        if theme is None:
            self.theme = "飞书机器人通用消息卡片模板"
        elif isinstance(theme, str):
            self.theme = theme
        else:
            raise TypeError("Theme must be an string.")

        if body is None:
            self.body = "🔹  内容模板:\n普通文本\n标准emoji 😁😢🌞💼🏆❌✅\n*斜体*\n**粗体**\n~~删除线~~\n[文字链接](https://www.feishu.cn)\n<at id=all></at>"
        elif isinstance(body, str):
            self.body = body
        else:
            raise TypeError("Body must be an string.")

        self._update()

    @property
    def OUTPUT(self) -> JSONType:
        # 序列化
        return json.dumps(self._contents)


# 单例模式
# BOT = _BOT()

