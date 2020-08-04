import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('div',class_= "VCSortableInPreviewMode")
tag2 = [tag.find('img') for tag in tags]
for tagz in tag2:
    try:
        print(tagz.get('src',None))
    except:
        print('EOF')    
    