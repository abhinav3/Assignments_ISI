import nltk
import sys
import codecs
import operator

filename = "rural.txt"

try:
    infile = codecs.open(filename,"r","UTF-8")
except IOError:
    print ("There was an error reading from",filename)
    sys.exit()
file_txt = infile.read()

tokens = nltk.word_tokenize(file_txt)
print(len(tokens))
infile.close()
trigram_tuples = list(nltk.trigrams(tokens))

dic = dict()
for w in trigram_tuples:
    if w in dic.keys():
        dic[w] = dic[w] + 1
    else:
        dic[w] = 1
        
try:
    outfile = codecs.open("trigram.txt","w","UTF-8")
except IOError:
    print ("There was an error writing to the file bigramm.txt")
    sys.exit()
sorted_dict = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)
for x in sorted_dict:
    outfile.write("(%s, %d)\n"%x)
outfile.close()
