import requests
import re
def geturl(link):
    req = requests.get(link)
    page = req.content.decode('utf-8','ignore')
    return page
url = 'http://lz.book.sohu.com/serialize-id-17129.html'
page = geturl(url)

lists = re.findall(r'/chapter.*?\.html',page)
for i in lists :
    try:
        Bpage = geturl('http://lz.book.sohu.com'+i)
        book = re.findall(r'<p><p>.*?</p></p>',Bpage)
    except:
        pass
    for bs in book:
        bs = re.sub(r'<p>|</p>','',bs)
        f = open('souhu.txt','a')
        f.write(bs+'\n\n')


