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
print (len(tokens))
infile.close()
