import time
import pyupbit
import datetime
import requests

myToken = "xoxb-4348614544996-4331639062583-VjfmGhoPvw4aDV4FhBoAC7kO"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": "Bearer "+token
            },
        data={"channel": channel,"text": text}
    )


# 시작 메세지 슬랙 전송
post_message(myToken,"#bitcoin", "autotrade start")

