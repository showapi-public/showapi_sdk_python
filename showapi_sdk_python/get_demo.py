# python3
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
# 文件上传demo
from showapi_request import ShowApiRequest
url = "https://route.showapi.com/64-19"
showapi_appid = '用户的appid'
showapi_sign = '用户的sercet'
r = ShowApiRequest (url, showapi_appid, showapi_sign)
r.setTimeout(15, 15)  # 超时设置，单位是秒
r.addBodyPara("com","zhongtong")
r.addBodyPara("nu","75312165465979")
res = r.get()
print(res.text) # 返回信息
print(res.content)# 返回信息【bytes型】
print(res.headers)# 返回头
print(res.status_code)# 返回状态