import nltk
import sys
import codecs
import operator
from nltk.stem import WordNetLemmatizer
import ast
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


filename = "rural.txt"

wordnet_lemmatizer = WordNetLemmatizer()

lines = [ line.rstrip('\n') for line in codecs.open(filename,"r","UTF-8")]

try:
    outfile = codecs.open("lemmatized_CORPUS.txt","w","UTF-8")
except IOError:
    print ("There was an error writing to the file lemmatizedunigramcontextf1.txt")
    sys.exit()


for content in lines:
   # currentline = content.split()
    tokens = word_tokenize(content)
    tokens_pos = pos_tag(tokens)
    for word in tokens_pos:
        wordnet_pos=get_wordnet_pos(word[1])
        if not (wordnet_pos == ''):
            lemmatized_word = wordnet_lemmatizer.lemmatize(word[0],wordnet_pos)
        else:
            lemmatized_word = wordnet_lemmatizer.lemmatize(word[0])
        outfile.write("%s "%(lemmatized_word))
    outfile.write("\n")
outfile.close()
#https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=7&ved=0ahUKEwjV-P-s8dTKAhVEBo4KHUKHDJoQFghFMAY&url=http%3A%2F%2Fmarcobonzanini.com%2F2015%2F01%2F26%2Fstemming-lemmatisation-and-pos-tagging-with-python-and-nltk%2F&usg=AFQjCNH2QDZsmW-zXwG8FnFFt1BxgMuLwQ&sig2=hUqMgeE2csdV6rfIblW7LA&cad=rja
