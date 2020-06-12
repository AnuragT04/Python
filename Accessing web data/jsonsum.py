import urllib.request, urllib.parse, urllib.error
import json
sum=0
url = input('Enter - ')
data = urllib.request.urlopen(url).read()
data=data.decode()
info=json.loads(data)
for item in info['comments']:
    sum=sum+int(item['count'])
print(sum)
