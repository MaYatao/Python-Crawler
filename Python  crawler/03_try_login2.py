import requests

url="http://www.renren.com/967947820/profile"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Cookie": "anonymid=jluafcqw-jm68fi; depovince=HUB; _r01_=1; JSESSIONID=abcBgc_maQXR79P-xv8ww; ick_login=1d9f7a66-b9d6-4a81-b75a-6b1ce3c67180; ick=39d6a9a0-fd54-406c-ad2d-bd3513fa2a25; XNESSESSIONID=69600c6bafcc; WebOnLineNotice_967947820=1; jebe_key=2c7171d0-4fc8-4125-b736-492bfa981011%7C2d06c43c34b8bcf5b0c194861f13822b%7C1536463602823%7C1%7C1536463601770; wp_fold=0; jebecookies=11fa9224-5a01-42e5-9227-e08c0a0e1733|||||; _de=C5650F2A1ECA839B1E2A0BF6B0527A4C; p=55aadd86ab7ae4fe427272085ad3e7560; first_login_flag=1; ln_uact=15836612714; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=bc242c5225681737cf17c8a615b429260; societyguester=bc242c5225681737cf17c8a615b429260; id=967947820; xnsid=43a1619d; ver=7.0; loginfrom=null"
}

response=requests.get(url,headers=headers)

with  open("renren2.html","w" ,encoding="utf-8")  as f:
    f.write(response.content.decode())