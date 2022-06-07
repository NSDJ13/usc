from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('FuEvlfP48sxUD0BJk0Jb6OV7Q9UgZsgLbUoPU8RnjeRlDYbgjO7XaCzWeJWUK1HOsmdPDP4fy/QtTwxLL4ROeCfndx7sLa/9hj5KCyg2K08WPKU0Gkw986oydNsdKpXKVfupQtyYEc2x3FUbVlXi/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0a7cffee6d50ababa6e75cac223bd636')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
