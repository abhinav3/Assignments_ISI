import nltk
from nltk.corpus import gutenberg
from nltk.collocations import *

with open('rural.txt') as f:
    text = f.read()
words = nltk.word_tokenize(text)
try:
    fout = open("chisq_bigrams.txt","w")
except IOError:
    print("Err")
    sys.exit()

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(words,window_size = 3);
for x in finder.nbest(bigram_measures.chi_sq,-1):
    #print(x)
    fout.write("%s , %s\n"%(x))
fout.close()
