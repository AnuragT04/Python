
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
pos=int(input())
rep=int(input())
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
for i in range(rep):
    tags = soup('a')
    print(tags[pos-1])
    x=tags[pos-1].get('href',None)
    html = urllib.request.urlopen(x).read()
    soup = BeautifulSoup(html, 'html.parser')
