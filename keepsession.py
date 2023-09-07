import http.cookies
import requests
import json
import time

# cookie_string = "Authorization=eyJOR3xyEPGYYg88SBKwLLVF4YbspERVXSLK.eyJ17WDNVh83TpBnrEBpuGRNFtDVKpnWynUTmVRaL22Q7MsUZgPgT7hmDvxm68bf6pMD3g.dgLLR6EhU-3gtVFSwhcenRqZMPd7yzq2bULMApKeGN8KbweFE2jHJHes4PDwxxwNwSKdDtF3EG8VnrPqTFaudVbydcUGgQbaVxRSgbBVCsC6eRL7-entRnGyr5Q3bEcWKaBJM8DMwPh3RtR7DnwtdXFg2mLdUMthhDynj9R-bNErdzQt7zK8k9F9HPfVxzdaVcmBUgwcp2YqUP-wNVhfwBJu2XpvawJPNNEhEHeBP7ysU7BTXNLvyn5H3-Lns93S7kapG-Ugn8wkk3Hg8svAbfwTu2W7RbxVr_Yud_9EBJ5h7TVG2PebYdqf7C_vK2wKJLkMqegy94dyhP6ba_6vdx; SERVERID=545b6d8d091f13d9ce1bf0321587bf07|1633082400|1633082400; SERVERID=f7dde79ccada9f4171454d57b0848c4a|1633082400|1633082400"
cookie_string ="Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjQwNTgyNzEzLCJzY2hJZCI6OTIsImV4cGlyZUF0IjoxNjk0MDkyODE4fQ.otf4qx0r4Zl4AQpuB2nChhgDeNFl7sD2vd22HdGvQjMdLIXf6VzbrQeqIQ5bvX5FmOZf3fWTHfYwrsl56uITZdtj1godgZN-m0f7rP1FVn5FLQb-1OQKZ0XWjAPnK_5396wCcwzi9YLydarcN31uyWN-h4l-JNm2McvBGgfx3HqKSocyJImMYd9BfEE1t4ZHeFuqOgzAf1u_NpNcSl17m1jnZeYSCgPfFnjwUF8LfQktvDaWk6ViLdl8iZbQDhFCE56VerFrdDYHX-xMFjwkFrMrTZU5-OmwbsvQvAm2ju--dC7OaIMOMnA1Kg3TCS28jcpD5aRBLoi6_bTQXg8z0g; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1694085623|1694085623; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1694085618|1694085618"
session = requests.Session()
cookie = http.cookies.SimpleCookie()
cookie.load(cookie_string)
for key, morsel in cookie.items():
    session.cookies.set(key, morsel)

while True:
    if session.cookies.keys().count("Authorization") > 1:
        session.cookies.set("Authorization", domain="", value=None)
    res = session.post("http://wechat.v2.traceint.com/index.php/graphql/", json={
        "query": 'query getUserCancleConfig { userAuth { user { holdValidate: getSchConfig(fields: "hold_validate", extra: true) } } }',
        "variables": {},
        "operationName": "getUserCancleConfig"
    })
    try:
        result = res.json()
    except json.decoder.JSONDecodeError as err:
        print("Error: %s" % err)
        break
    if result.get("errors") and result.get("errors")[0].get("code") != 0:
        print("Session expired!")
        break
    print("Session OK.")
    time.sleep(60)