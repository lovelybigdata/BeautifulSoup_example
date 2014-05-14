# 先將第8章的範例的第一個部份 註解後上傳至此

#scraper for packtpub, amazon , barnes&noble for comparing selling price.

import urllib2
import re
from bs4 import BeautifulSoup

packtpub_url = "http://www.packtpub.com/"

def get_bookurls(url): 

# 這個函數是用來執行下一頁的動作 並且把回傳網址 
# 例如 http://www.packtpub.com//books/all?page=31
# http://www.packtpub.com//books/all?page=32
# http://www.packtpub.com//books/all?page=33
# http://www.packtpub.com//books/all?page=34

   req = urllib2.Request(url, headers={'User-Agent' : "Magic-NIKE  Browser"}) 
   page = urllib2.urlopen(req)
   soup_packtpage = BeautifulSoup(page,"lxml")
   page.close()
   next_page_li = soup_packtpage.find("li",class_="pager-next last")

   if next_page_li is None:
       next_page_url = None
       print "OK Finish " # 顯示結束
   else:
       next_page_url = packtpub_url + next_page_li.a.get("href")
       print next_page_url  # print 的指令單純是用來確認目前執行的進度  因為總共有50個頁面所以時間上會有一點久
       return next_page_url


start_url = "http://www.packtpub.com/books"
continue_scrapping = True
books_url = [start_url]

# 程式主要是從這裡開始執行的 因為不知道會執行幾次 所以使用的是 while 語法
# 如果沒有下一頁的時候就停止執行
# 如果有下一頁的話，就呼叫 get_bookurls

while continue_scrapping:
	next_page_url= get_bookurls(start_url)
	if next_page_url is None:
		continue_scrapping = False
	else:
		books_url.append(next_page_url)
		start_url = next_page_url
