# 导入库
import requests
import re
import wordcloud

from wordcloud import WordCloud
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
# 查询BV号
BV = input("请输入BV号：")
BVurl = "https://m.bilibili.com/video/" + BV
def Run(BVurl):
    response1 = requests.get(BVurl, headers)
    # js_str = response1.content.decode()
    # 正则筛选
    data = re.findall(r'"cid":[\d]*', js_str)
    data = data[0].replace('"cid":', "").replace(" ", "")
    url = "https://comment.bilibili.com/{}.xml".format(data)
    response2 = requests.get(url, headers).content.decode()
    Danmu = re.findall('<d.*?>(.*?)</d>', response2)
    Danmu_str = " ".join(Danmu)
    # 设置词云图参数
    w: WordCloud = wordcloud.WordCloud(font_path='msyh.ttc', background_color='white', width=1200, height=600)
    # 生成词云图和保存
    w.generate(Danmu_str)
    w.to_file('WordCloud.png')