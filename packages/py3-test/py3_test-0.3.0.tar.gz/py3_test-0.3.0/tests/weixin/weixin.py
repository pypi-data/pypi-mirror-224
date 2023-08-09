import json
import os
import time

import requests


class Weixin:
    """
    save corp_id, secret
    save token and refresh every 7200 Seconds
    """

    URL_GET_TOKEN = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"  # get method, 1)corpid,2)corpsecret
    URL_SEND_MSG = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="  # access_token=ACCESS_TOKEN, post method
    TOKEN_COTENT = ".TOKEN_CONTENT"
    TOKEN_TIMESTAMP = ".TOKEN_TIMESTAMP"

    def __init__(self):
        self._corp_id = "wx12e5bb9ec21908f5"
        self._secret = "c0pWa6jszc_SRZ1Xnm9jaJrtnY2io9TxH4ITfQq3WiI"
        self._touser = "@all"
        self._toparty = "12"
        self._agentid = 1000004
        self.diff = 7000

    def send(self, text):
        token = self.refresh_token()
        payload = {
            "touser": self._touser,
            "toparty": self._agentid,
            "msgtype": "text",
            "agentid": self._agentid,
            "text": {"content": str(text)},
            "safe": "0",
        }
        response = requests.post(
            self.URL_SEND_MSG + token, data=json.dumps(payload, ensure_ascii=False)
        )
        response_json = response.json()
        print(response_json)

    def refresh_token(self):
        token = ""
        last_time = 0
        need_refresh = False
        if os.path.exists(self.TOKEN_TIMESTAMP):
            f_time = open(self.TOKEN_TIMESTAMP)
            last_time = float(f_time.read())

        current_time = time.time()
        if current_time - last_time > self.diff:  # need refresh
            need_refresh = True

        if not os.path.exists(self.TOKEN_COTENT):
            need_refresh = True

        if need_refresh:
            f_time = open(self.TOKEN_TIMESTAMP, "w")
            f_time.write(str(time.time()))
            f_time.close()

            payload = {"corpid": self._corp_id, "corpsecret": self._secret}
            response = requests.get(self.URL_GET_TOKEN, params=payload)
            response_json = response.json()
            print(response_json)

            token = response_json["access_token"]
            f_content = open(self.TOKEN_COTENT, "w")
            f_content.write(token)
            f_content.close()
        else:
            f_content = open(self.TOKEN_COTENT)
            token = f_content.read()
            f_content.close()
        return token


if __name__ == "__main__":
    weixin = Weixin()
    content = "测试"
    weixin.send(content)
