import  requests
import  json

url="https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=0"

headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
"Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288"
}

response=requests.get(url,headers=headers)
json_str=response.content.decode()

ret1=json.loads(json_str)  #python转化成json字符串

with  open("douban.txt","w" ,encoding="utf-8")  as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=2))
    #dumps()将python类型转化成json