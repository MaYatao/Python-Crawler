import requests

#实例化sesssion 
session=requests.session()

#使用session发送post请求，获取对方保存在本地的cookie
post_url="http://www.renren.com/PLogin.do"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Referer": "http://www.renren.com/"
}

post_data={"eamil":"15836612714","password":"123456789"}

session.post(post_url,headers=headers,data=post_data)


url="http://www.renren.com/967947820/profile"
response=session.get(url,headers=headers)

with  open("renren4.html","w" ,encoding="utf-8")  as f:
    f.write(response.content.decode())


