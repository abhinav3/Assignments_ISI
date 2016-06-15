import nltk
import json
from operator import itemgetter
import pickle
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.util import ngrams


window_size = 3 

wfd = FreqDist()
bfd = FreqDist()
wfdr = FreqDist() 


f = open("rural.txt","r")
text = f.read()
f.close()
sents = nltk.sent_tokenize(text)

nbgrams = 0


for sent in sents:                                  
    words = [w.lower() for w in nltk.word_tokenize(sent) if (not (len(w)==1 and (not w.isalpha()) ) )]
    for window in ngrams(words, window_size, pad_right=True):
        w1 = window[0]
        if w1 is None:
            continue
        
        for w2 in window[1:]:
            if w2 is not None:
                bfd[(w1, w2)] += 1
                nbgrams += 1
                wfd[w1] += 1
    #Reverse the list of words
    words.reverse()
    for window in ngrams(words, window_size, pad_right=True):
        w1 = window[0]
        if w1 is None:
            continue

        for w2 in window[1:]:
            if w2 is not None:
                wfdr[w1] += 1
cnt = 0
collo = []
for k,v in bfd.items():
    if v < 10.0:     #Should occur at least 10 times in the corpus
        continue

    o11 = float(v)
    o12 = float(wfdr[k[1]] - v)      #first absent second present
    o21 = float(wfd[k[0]] - v)          # first present second absent
    o22 = float(nbgrams - wfd[k[0]] -  wfdr[k[1]] + v)

    chi_sqr = (nbgrams*((o11*o22 - o12*o21)**2))/((o11+o12)*(o11+o21)*(o12+o22)*(o12+o22))

    if chi_sqr >= 3.841:
        cnt += 1
        
        collo.append([k[0], k[1], chi_sqr])

sorted_collo = sorted(collo, key=itemgetter(2), reverse=True)


f1 = open("collocations.txt","w")
for item in sorted_collo:
    item[2] = str(item[2])
    f1.write(" ".join(item))
    f1.write("\n")

f1.close()

