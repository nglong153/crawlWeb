import urllib.request,urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = 'https://uet.vnu.edu.vn/category/sinh-vien/hoc-phi-hoc-bong/'
req = urllib.request.urlopen(url).read()
# soup time
soup = BeautifulSoup(req,'html.parser')

lookingForTag = soup.findAll('div',class_ = 'item-content')
hocBong = [tag.find('a').text for tag in lookingForTag]

lookingForTag = soup.findAll('div',class_ = 'month')

for i in range (0,len(hocBong)):
    print(hocBong[i] + '---' + lookingForTag[i].text)