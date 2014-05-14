BeautifulSoup_example
=====================
BeautifulSoup4的範例

在 123 的那個分支其中的程式碼
有的可能無法執行
因為書商後來有擋掉，如果直接按照書中的做法
可能會有問題會直接回傳 403 error
google後發現主要的異常是網站供應商特意擋掉的
因為另外2個網站是沒有這個問題

http://www.barnesandnoble.com/
http://www.amazon.com/


原本的這個程式碼
page = urllib2.urlopen(url)

要修正成
req = urllib2.Request(url, headers={'User-Agent' : "Magic-NIKE  Browser"}) 
page = urllib2.urlopen(req)

要先騙過網站，我是利用 browser 看網頁的...

所以後續會將修正版的放在 master 分支中



