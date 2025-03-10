# pip install websocket

import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time
import websocket
import logging

class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = "48317e28"
        self.APIKey = "7a802755f632dfb2dffd314ca86866e9"
        self.APISecret = "ZWJmZjlkOTU4YTUyMDBhY2RkOTBiOGNl"
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path

        self.gpt_url = "ws://cn-huadong-1.xf-yun.com/v1/private/vms_cloud_edge_ctrl"

    # 生成url
    def create_url(self):
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        print("dateStr->",date)

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        print("signature_origin->",signature_origin)

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        print("signature_sha type->",type(signature_sha))
        print("signature_sha->", signature_sha)
        print("signature_sha- len>", len(signature_sha))

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        print("signature_sha_base64->", signature_sha_base64)

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        print("authorization_origin->", authorization_origin)

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        print("authorization->", authorization)
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.gpt_url + '?' + urlencode(v)
        print("url->", url)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url


# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws,arg1,arg2):
    print("### closed ###",ws,arg1,arg2)


# 收到websocket连接建立的处理
def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, question=ws.question))
    ws.send(data)


# 收到websocket消息的处理
def on_message(ws, message):
    data = json.loads(message)
    code = data['header']['code']
    status = data['header']["status"]
    print(status)
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        print(data)

        if status == 2:
            ws.close()


def gen_params(appid, question):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": "48317e28",
            "uid": "u123"
        },
        "parameter": {
            "auditory_sense": {
                "vcn":"x4_lingxiaoxuan_chat",
                "speed": 50,
                "pitch": 50,
                "volume": 50,
                "callback_pybuf": 1,
                "source":"aiui"
            },
            "vision_control": {
                "anchor_id": "131011001",
                "lips_flow": {
                    "format": "json"
                }
            }
        },
        "payload": {
            "text": {
                "compress": "raw",
                "encoding": "utf8",
                "format": "plain",
                "text": "PHNwZWFrPuS7iuWkqeWkqeawlOaAjuS5iOagtzwvc3BlYWs+"
            }
        }
    }
    return data


def main(appid, api_key, api_secret, gpt_url, question):
    wsParam = Ws_Param(appid, api_key, api_secret, gpt_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    # 测试时候在此处正确填写相关信息即可运行
    main(appid="48317e28",
         api_key="7a802755f632dfb2dffd314ca86866e9",
         api_secret="ZWJmZjlkOTU4YTUyMDBhY2RkOTBiOGNl",
         gpt_url="ws://cn-huadong-1.xf-yun.com/v1/private/vms_cloud_edge_ctrl",
         question="<speak>今天天气怎么样</speak>")