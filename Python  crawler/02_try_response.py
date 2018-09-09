import  requests

url="https://fanyi.baidu.com/basetrans"

data={
    "query":"人生苦短，我用python",
    "from": "zh",
    "to": "en"  }
headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047"
}
response=requests.post(url,data=data,headers=headers)

print(response.content.decode())