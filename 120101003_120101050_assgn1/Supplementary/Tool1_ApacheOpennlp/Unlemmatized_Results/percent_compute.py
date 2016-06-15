import re
import sys



result=0
count=0
total=0

with open("bi.csv","r") as f:
    for line in f:
        #a = 'lkdfhisoe78347834 (())&/&745  '
        if(re.sub('[^0-9]','', line)==''):
            pass
        else:
            total = total + int(re.sub('[^0-9]','', line))

total=int(total*0.8)
with open("bi.csv","r") as f:
    for line in f:
        #a = 'lkdfhisoe78347834 (())&/&745  '
        if(re.sub('[^0-9]','', line)==''):
            pass
        else:
            result = result+int(re.sub('[^0-9]','', line))
            count+=1
            if (result>=total):
                print(count)
                sys.exit(0)

print (result)
