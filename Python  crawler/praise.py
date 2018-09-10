from  retrying  import  retry
import requests


headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
"Referer": "https://m.douban.com/tv/american"
}
@retry(stop_max_attempt_number=3)  #让被装饰的函数反复执行三次，三次全部报错才报错，中间一次正常就不报错
def  _prase_url(url):
    print('****')
    response=requests.get(url,headers=headers,timeout=5)
    return  response.content.decode()

def  prase_url(url):
    try:
        html_str=_prase_url(url)        
    except :
        html_str=None
    return  html_str

if __name__  =='__main__':
    url="http://www.baidu.com"
    print(prase_url(url)[:100])

