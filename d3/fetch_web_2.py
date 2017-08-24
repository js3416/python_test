import datetime, time
import urllib.request
#import operator

f = urllib.request.urlopen('http://www.yonhapnews.co.kr/bulletin/2016/08/15/0200000000AKR20160815027000001.HTML')
data = f.read().decode('utf-8')
#data = f.read()
data = data.replace(".", "")
data = data.replace(",", "")
data = data.replace("'", "")
data = data.replace('"', '')
data = data.replace('</p>', '')
data = data.replace('<p>', '')

start = data.find("「")-1
end = data.find("」")

content = data[start:end]

content = content.split()

anal = {}
for word in content:
    anal[word] = anal.get(word, 0) +1



#newlist = sorted(anal.values(), reverse=True)
#newlist = sorted(anal.items(), key=operator.itemgetter(1), reverse=True)
newlist = sorted(anal.items(), key=lambda kv: kv[1], reverse=True)
c=0
print("number of words =", len(newlist))
for k,v in newlist:
    print(k,v)
    #print(word)
    c+=1
    if c > 20: break
        
#print(len(content))
#print(content)
