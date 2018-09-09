import  requests
import json

url="https://fanyi.baidu.com/basetrans"

query_str=input("请输入要翻译的中文：") 

data={
    "query":query_str,
    "from": "zh",
    "to": "en"  }
headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047"
}
response=requests.post(url,data=data,headers=headers)

html_str=response.content.decode()  #json字符串
# type()检查数据类型
#print(type(response.content.decode()))

dirt_ret=json.loads(html_str)  #转换位json字典

ret=dirt_ret["trans"][0]["dst"]

print("翻译结果是：",ret)
