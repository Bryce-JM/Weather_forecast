import requests
from lxml import etree

url = "https://s.weibo.com/top/summary/"

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

response = requests.get(url, headers=headers)
html = response.text

html = etree.HTML(html)

topic = html.xpath('//tr[@class]/td[@class="td-02"]/a')      # 标签
heat = html.xpath('//tr[@class]/td[@class="td-02"]/span')    # 热度
topic_URL = html.xpath('//tr[@class]/td[@class="td-02"]/a/@href')      # 网址

def delete(html):
    data = html.xpath('//div[@class="card card-no-result s-pt20b40"]')
    if data:
        print("被撤")
    else:
        print("正常")

lis = ["https://s.weibo.com/weibo?q=%23苹果上架香港暴徒好帮手app%23&Refer=SWeibo_box"]
for x in topic_URL:
    lis.append("https://s.weibo.com" + x)

for url in lis:
    response = requests.get(url, headers=headers)
    html = response.text

    html = etree.HTML(html)
    delete(html)



# 保存到字典
# dst = {}
# for x in range(50):
#     dst[topic[x+1].text] = heat[x].text
# print(dst)


