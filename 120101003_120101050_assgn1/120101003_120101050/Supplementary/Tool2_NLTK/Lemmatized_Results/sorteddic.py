import nltk
import sys
import codecs
import operator

filename = "lemmatizedunigramcontextf1.txt"

try:
    infile = codecs.open(filename,"r","UTF-8")
except IOError:
    print ("There was an error reading from",filename)
    sys.exit()
file_txt = infile.read()

tokens = nltk.word_tokenize(file_txt)
print(len(tokens))
infile.close()

dic = dict()
for w in tokens:
    if w in dic.keys():
        dic[w] = dic[w] + 1
    else:
        dic[w] = 1
        
try:
    outfile = codecs.open("unigram.txt","w","UTF-8")
except IOError:
    print ("There was an error writing to the file sorteddic.txt")
    sys.exit()
sorted_dict = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)
for x in sorted_dict:
    outfile.write("%s,%d\n"%x)

    
dict1=dict(sorted_dict)
i = 0
for x in dict1:
    dict1[x]=i
    i = i + 1
outfile.close()

try:
    dictfile = codecs.open("dictionary.txt","w","UTF-8")
except IOError:
    print ("There was an error writing to the file dictionary.txt")

for x in dict1:
    dictfile.write("%s : %d \n"%(x,dict1[x]))
dictfile.close()
