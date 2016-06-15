import nltk
from nltk.util import ngrams
from nltk.corpus import gutenberg
from collections import Counter

#testVar = raw_input("Give path")
#print testVar
#fo = open(testVar, "wb")
count = 0
testStr = ""
testWord = ""
dictWords = []
wordsFornGram = []
with open("rural.txt", 'r') as f:
     for line in f :
        i = 0
        #print line
        while i < len(line) :
            if line[i] != '.' and line[i] != '!' and line[i] != '?':
                testStr = testStr + line[i]
                if line[i]==' ' or line[i]=='\n':
                    if testWord != "" :
                        wordsFornGram.append(testWord.lower())
                    if testWord in dictWords:
                        if count == 0 :
                            print ("hii")
                    else :
                        if count == 0 :
                            print ("%s"%testWord)
                        dictWords.append(testWord.lower())
                    testWord = ""
                else:
                    testWord = testWord + line[i]
                i=i+1
            elif line[i]=='!' or line[i]=='?':
                if testWord != "" :
                    wordsFornGram.append(testWord.lower())
                if testWord in dictWords:
                    if count == 0 :
                        print ("hii")
                else :
                    if count == 0 :
                        print ("%s\n"%testWord)
                    dictWords.append(testWord.lower())
                testWord = "" 
                if i+1 < len( line ) and line[i+1].isupper :
                #   print count
                #   print testStr
                    testStr=""
                    count=count+1
                else :
                    testStr = testStr + line[i]
                i=i+1
            elif line[i]=='.' :
                if testWord != "" :
                    wordsFornGram.append(testWord.lower())
                if line[i-2:i-1]!="Dr" or line[i-2:i-1]!="Mr" or line[i-2:i-1]!="vs" or line[i-3:i-1]!="Mrs" or line[i-3:i-1]!="etc" : 
                #   print count
                #   print testStr
                    testStr=""
                    count=count+1
                    print ("%d \n"%count)
                else :
                    testStr = testStr + line[i]
                if testWord in dictWords:
                    if count == 1 :
                        print ("hii")
                else :
                    if count == 1 :
                        print ("%s\n"%testWord)
                    dictWords.append(testWord.lower())
                testWord = ""

                i=i+1
f.close()
n=1
try:
   f1 = open("uni.txt","w")
except IOError:
   print ("Err uni")
try:
   f2 = open("bi.txt","w")
except IOError:
   print ("Err bi")
try:
   f3 = open("tri.txt","w")
except IOError:
   print ("Err tri")

unigrams = ngrams(wordsFornGram, n)
#print (len(unigrams))
unigrams_freq = Counter(unigrams)
unigrams_sorted =  unigrams_freq.most_common()
for x in unigrams_sorted:
   f1.write("%s\n"%(x,))
n=2
bigrams = ngrams(wordsFornGram, n)
#print (len(bigrams))
bigrams_freq = Counter(bigrams)
bigrams_sorted =  bigrams_freq.most_common()
for x in bigrams_sorted:
   f2.write("%s\n"%(x,))
n=3
trigrams = ngrams(wordsFornGram, n)
#print (len(trigrams))
trigrams_freq = Counter(trigrams)
trigrams_sorted =  trigrams_freq.most_common()
for x in trigrams_sorted:
   f3.write("%s\n"%(x,))
f1.close()
f2.close()
f3.close()
