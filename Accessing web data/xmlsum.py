import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum=0
url = input('Enter - ')
data = urllib.request.urlopen(url).read()
data=data.decode()
tree=ET.fromstring(data)
list=tree.findall('comments/comment')
for item in list:
    sum=sum+int(item.find('count').text)
print(sum)
