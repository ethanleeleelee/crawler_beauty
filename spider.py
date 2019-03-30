import requests
from bs4 import BeautifulSoup
import datetime

def beauty(times):
    x = datetime.datetime.now()
    amount = 1
    url_pages = "https://www.ptt.cc/bbs/Beauty/index.html"
    for t in range(times):
        r1 = requests.get(url_pages)
        source_page = BeautifulSoup(r1.text, "html.parser")
        sel_prev = source_page.select("div.btn-group.btn-group-paging a")
        #得到上頁網址
        prev = "https://www.ptt.cc" + sel_prev[1]['href']
        #點進標題網址
        sel = source_page.select("div.title a")
        for s in sel:
            #print("https://www.ptt.cc" + s['href'])
            url = "https://www.ptt.cc" + s['href']
            r = requests.get(url)
            source = BeautifulSoup(r.text, "html.parser")
            data = []
            data.append(source.find_all("div", "article-metaline"))
            data.append(source.find_all("div", "richcontent"))
            source2 = BeautifulSoup(str(data), "html.parser")
            images = source2.find_all("a")
            print("this is from " + url)
            #print(images)
            for i in images:
                #製造正確網址
                image_url = "https://i."+ i['href'][2:] + ".jpg"
                #爬圖
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
                pic = requests.get(image_url, headers=headers)
                print("number" + str(amount))
                #寫入本地資料庫
                img1 = pic.content
                img_out = open("spider/"+str(x.year)+str(x.month)+str(x.day)"img"+str(amount)+".png", "wb")
                img_out.write(img1)
                img_out.close()
                amount+=1
        url_pages = prev
    print("finish!")

beauty(2)