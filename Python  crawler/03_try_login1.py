import requests

url="http://www.renren.com/967947820/profile"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",

}

response=requests.get(url,headers=headers)

with  open("renren1.html","w" ,encoding="utf-8")  as f:
    f.write(response.content.decode())