#需要安装：  pip install requests
import requests
#以下需要修改
appcode="xxxxx"
req_data = {
    'nu': 'YT4620020577123',
}
#修改结束
url="http://ali-deliver.showapi.com/fetchCom"
headers = {
    'Authorization':'APPCODE ' + appcode
}

try:
    html = requests.get(url, headers=headers,data=req_data)
except :
    print("URL错误")
    exit()
print("---------response status is:-------------")
print(html.status_code )
print("---------response headers are:-------------")
print(html.headers)
msg = html.headers.get('X-Ca-Error-Message')
status=html.status_code

if status == 200 :
    print("status为200，请求成功，计费1次。（status非200时都不计费）")
else:
    if(status == 400 and msg == 'Invalid AppCode'):
            print("AppCode不正确，请到用户后台获取正确的AppCode： https://market.console.aliyun.com/imageconsole/index.htm")
    elif(status == 400 and msg == 'Invalid Path or Method'):
            print("url地址或请求的'GET'|'POST'方式不对")
    elif(status == 403 and msg == 'Unauthorized'):
            print("服务未被授权,请检查是否购买")
    elif(status == 403 and msg == 'Quota Exhausted'):
            print("套餐资源包次数已用完")
    elif(status == 500 ):
            print("API网关错误")
    else:
            print("参数名错误或其他错误")
            print(status)
            print(msg)

print("---------response body is:-------------")
print(html.text)
