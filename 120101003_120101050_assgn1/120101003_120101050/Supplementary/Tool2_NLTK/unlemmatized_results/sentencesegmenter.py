import nltk
import sys
import codecs
filename ="rural.txt";
#filename = input("Enter corpus filename")
try:
    infile = codecs.open(filename,"r","UTF-8")
except IOError:
    print ("There was an error reading from ",filename)
    sys.exit()

text = infile.read()
infile.close()

sent_tokens = nltk.sent_tokenize(text)
print (len(sent_tokens))

try:
    outfile = codecs.open("segmentedsentence.txt","w","UTF-8")
except IOError:
    print ("There was an error writing to the file segmentedsentence.txt")
    sys.exit()

for x in sent_tokens:
    outfile.write("%s\n\n"%x)

outfile.write("\n")

outfile.close()
