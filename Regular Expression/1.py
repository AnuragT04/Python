import re
file=input()
fh=open(file)
sum=0
for line in fh:
    y=re.findall('[0-9]+',line)
    if len(y)==0:   continue
    for x in y:
        sum=sum+int(x)
print(sum)
