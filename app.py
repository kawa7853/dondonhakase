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

line_bot_api = LineBotApi('eiU2ukPs7rTJzafjqnUES1B2r79dhNm7zQ+Rg67d02bWT70iwmaBjEM+BJhZ3XzbgKecJTkZlbLcqBDcyLsY3TTZ1zkDtNwXwTosdKW4W+ceN1YbHObW7VKnprHfp5u0dxCd9AqBXpf5kZBXaDe8dAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3207086038d4d11fb7bfe5513fe35eb0')

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
    r = "やん？"

    if msg in ["hi", "Hi"]:
        r = "やん〜"
    elif msg == "ドンドン博士":
        r = "やん！"
    elif msg == "今田美桜":
        r = "かわいい、セックスしたい！"
    if msg == "問題":
        r = "問題はなにやん?"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = r))


if __name__ == "__main__":
    app.run()