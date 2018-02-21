import requests
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    '1E5ng3qycNMSrT+KvswesMPOCPTT9DMZ7mzvLSaMzx9ySpY4xyp4WJ6QWorkl1cB6YH3eX3pHSTMI2XqZ1JDLYLF7PB42uFmfPPh5BCHdV+1z9WS14C21XMcZOx+2izJiEmjulXxuZHhZggWx0cw4QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7e3c439fc6fbd60e8e88b7b9a69a6259')

# 監聽所有來自 /callback 的 Post Request


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    sentGoogleSheet(event.message.text)
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)


def sentGoogleSheet(messageText):
    r = requests.get(
        "https://script.google.com/macros/s/AKfycbyjODcLO3-5jIqgkCy83fi9NZLz8kL_wRAT2CixKFA4/exec?data="+messageText+",rr,rrr&sheetUrl=https://docs.google.com/spreadsheets/d/1wOt1WAQ6puQAK63fHMpCS1D34wWvWqCqM_odNmqFW_U/edit&sheetTag=sheet1")


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
