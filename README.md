# lark-robot-message

快速搭建一个飞书机器人消息卡片的 HTTP 服务（基础卡片）。

## 使用示例

```shell
# 1.服务运行
[admin@localhost ~]$ ./lark-robot-message/manage.py
 * Serving Flask app 'src' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8000
 * Running on http://xx.xx.xx.xx:8000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 139-674-975


# 2.编写消息请求
[admin@localhost ~]$ vim call.sh
#!/bin/sh

curl --location --request POST 'http://127.0.0.1:8000/api/robot-msg' \
--header 'Authorization: Token xxxxxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "xxxxxx@gmail.com",
    "title": "测试标题",
    "content": "测试内容😊: \nPart 01\nPart 02"
}'

#EOF


# 3.服务调用
[admin@localhost ~]$ yum -y install jq

[admin@localhost ~]$ sh call.sh | jq .
{
  "code": 0,
  "msg": "success",
  "data": {
    "email": "xxxxxx@gmail.com",
    "title": "测试标题",
    "content": "测试内容😊: \nPart 01\nPart 02"
  }
}
```
