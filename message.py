import time
import pyupbit
import datetime
import requests

myToken = ""

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": "Bearer "+token
            },
        data={"channel": channel,"text": text}
    )


# 시작 메세지 슬랙 전송
post_message(myToken,"#bitcoin", "autotrade start")
print("start")

