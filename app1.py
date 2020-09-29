#Line 兩個最有名套件 flask, django

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('egMcTdJqEZ1oB0Zt/rU1R+mhQgUSzaYqMoZ12lo1nQe6rNO3A3FqBVsuwA3HlGbiVW8kdMdjmzcbPU6EuUaPZDQRPqnK5Aax4RGmSN1Xk8DXsu9Q1PhRXWdIU9+cjLcrjw9FHbLthSNea+/nOviovAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bda4ec429b74bddaf27961fd05cb28aa')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = "安安"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = msg))


if __name__ == "__main__":
    app.run()