import json
import time

import requests

header = {
    "Host": "wechat.v2.traceint.com",
"Connection":"keep-alive",
"Content-Length": "349",
"App-Version": "2.0.14",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8379 Flue",
"Content-Type": "application/json",
"Accept": "*/*",
"Origin": "https://web.traceint.com",
"Sec-Fetch-Site": "same-site",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://web.traceint.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh",
"Cookie": "FROM_TYPE=weixin; v=5.5; wechatSESS_ID=073cccba0f9f44c9cc1d6fb24026252d9e91ff19807a7446; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjQwNTgyNzEzLCJzY2hJZCI6OTIsImV4cGlyZUF0IjoxNjk0MDgzMjgzfQ.EQTocOH7roDM3lq22gXomMaeL7kZW5Q3jEkd4i8D1KhdgJ-yhlAPX7u6dpZrifS1u385mdYi-y9BpVBOBHQRSsfhiCUrU6babynYDt9B2GpDjGBXnVnSipwXcy13VskfAO720CzDMJSYGnkQCD7Wm6Z3dDdFIq2UhFHa8hxiYyBlE-TEOL6QtTNFzPisDDsqjQ8l3uklbqs1RcKJejWjt3f-iCqdqLRv901g5NRYHKwOrp7goyVZyExHb0N6b2uyGLDlF1RFVfe3nUC-_upe0g5YOmU-UKcpEXGHbiu9p6fI5qNdhZ0y_F3-vcNfBRTcioP_n6n8z0g5DsAPJI6MbQ; Hm_lvt_7ecd21a13263a714793f376c18038a87=1694076084,1694077122; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1694080264; SERVERID=d3936289adfff6c3874a2579058ac651|1694080340|1694077120"
}
url = 'https://wechat.v2.traceint.com/index.php/graphql/'
data = {"operationName":"reserueSeat","query":"mutation reserueSeat($libId: Int!, $seatKey: String!, $captchaCode: String, $captcha: String!) {\n userAuth {\n reserve {\n reserueSeat(\n libId: $libId\n seatKey: $seatKey\n captchaCode: $captchaCode\n captcha: $captcha\n )\n }\n }\n}","variables":{"seatKey":"9,7","libId":313,"captchaCode":"","captcha":""}}
res = requests.post(url=url, headers=header, json=data)
tm = res.elapsed.total_seconds()# 获取请求时间

print(tm)
print(res.status_code)
print(res.text)
