import  json
from lxml  import etree
import requests

class  QiushiSpider:

    def  __init__(self):
        self.url_temp="https://www.qiushibaike.com/8hr/page/{}/"
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

    def get_url_list(self): #根据url地址规律构造url list
        url_list=[self.url_temp.format(i)   for i in range(1,14)]
        return url_list

    def prase_url(self,url):
        response=requests.get(url,headers=self.headers)
        return  response.content.decode()
        
    def  get_content_list(self,html_str): #提取数据
        html=etree.HTML(html_str)
        comment_list=[]
        #1.分组
        div_list=html.xpath('//div[@id="content-left"]/div')
        for  div  in div_list:
            item={}
            item["author_name"]=div.xpath(".//h2/text()")[0].strip()  if len(div.xpath(".//h2/text()")) >0 else  None
            item["content"]=div.xpath(".//div[@class='content']/span/text()")
            item["content"]=[i.strip()  for i  in item["content"]]
            item["stats-vote"]=div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats-vote"]=item["stats-vote"][0] if len(item ["stats-vote"])>0 else  None
            item["stats-comments"]=div.xpath('.//span[@class="stats-comments"]/a/i/text()')
            item["stats-comments"]=item["stats-comments"][0] if len(item["stats-comments"])>0 else  None
            item["img"]=div.xpath(".//div[@class='thumb']//img/@src")
            item["img"]=  "https"+item["img"][0] if len(item["img"])>0 else  None
            comment_list.append(item)

        return  comment_list

    def  save_content_list(self,content_list):
        with  open ("qiushibaike.txt","a",encoding="utf-8")  as f:
            for content  in  content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") 
        print("保存成功")

    def run(self):#实现主逻辑
        #根据url地址的规律，构造url_list
        url_list=self.get_url_list()

        for url  in url_list:
             #2.发送 请求，获取响应
            html_str=self.prase_url(url)

            #3.提取数据
            content_list=self.get_content_list(html_str)
             #4.保存
            self.save_content_list(content_list)
       
           

if __name__=="__main__":
    qiubai=QiushiSpider()
    qiubai.run()
    print("保存结束")