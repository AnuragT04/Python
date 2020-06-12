import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
sum=0
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags=soup('span')
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)
