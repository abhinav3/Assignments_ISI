#!/usr/bin/env python3
# encoding=utf-8
from __future__ import division
from Sentence import Sentence
from optparse import OptionParser
import sys
import cPickle
import operator
import re

class HMM:
    '''
  Vanilla trigram HMM tagger
    
    '''

    def __init__(self, train_filename, test_filename, tag_num):
        '''
        Constructor
        '''
        ''' ALLCAPS [A-Z-]+    :0
            NUM    \d+      :1
            FLOAT  [0-9]*[.][-]*[0-9]+ :2
            RARE    default :3
                '''
        
        self.RARE_WORD_COUNT = 5
        self.vocabsize=0
        self.word_count = {}
        self.word_tag_count = {}
        self.tag_uni_count = [0 for i in range(tag_num)]
        self.tag_bigram_count = [[0 for j in range(tag_num)] for i in range(tag_num)]
        self.tag_trigram_count = [[[0 for k in range(tag_num)] for j in range(tag_num)] for i in range(tag_num)]
        self.sents = [Sentence(tag_num)]
        self.total_tag = 0
        self.__rare_word = {}
    
        lines = open(train_filename).readlines()
        for i in range(len(lines)):
            line = lines[i].strip('\n')
            if len(line) > 0:
                wt = line.split('/')
              #  print (wt)
                tm = wt[:-1]
                st = wt[0]
                for j in range(1,len(tm)):
                    st= st +"_"+tm[j]
                
                self.sents[-1].add_word_tag(st, wt[-1])
        if(wt[-1] == "$"):
            self.sents[-1].finish(self.word_count, self.word_tag_count, self.tag_uni_count, self.tag_bigram_count, self.tag_trigram_count)
                self.total_tag += len(self.sents[-1].word_tag) - 2
                self.sents.append(Sentence(tag_num))
        self.sents[-1].finish(self.word_count, self.word_tag_count, self.tag_uni_count, self.tag_bigram_count, self.tag_trigram_count)
        self.total_tag += len(self.sents[-1].word_tag) - 2
        # self.word_prob = {}
        print(len(self.word_count))
        print(self.word_count['Germany'])
        print(self.word_count['Canada'])
        self.vocabsize=len(self.word_count);
        rarelist=[[0 for i in range(tag_num)]for j in range(4)]
        rc=[0 for i in range(4)]
        rf=[0 for i in range(4)]
        index=0
        for w in self.word_count.keys():
            if self.word_count[w] <= self.RARE_WORD_COUNT:
                self.__rare_word[w] = self.word_count[w]
                for i in range(tag_num):
                    index = 0
                    matchObj1 = re.match(r'[A-Z-]+',w)
                    matchObj2 = re.match(r'\d+',w)
                    matchObj3 = re.match(r'[0-9]*[.][-]*[0-9]+',w)
                    
                    
                    if not (matchObj1 is None):
                        #print(matchObj1.group(0))
                        rarelist[0][i] += self.word_tag_count[w][i]
                        rc[0] += 1
                        
                    elif not (matchObj2 is None):
                        #print(matchObj2.group(0))
                        rarelist[1][i] += self.word_tag_count[w][i]
                        rc[1] += 1
                        index =1
                    elif not (matchObj3 is None):
                        #print(matchObj3.group(0))
                        rarelist[2][i] += self.word_tag_count[w][i]
                        rc[2] += 1
                        index = 2
                    else:
                        #print(w)
                        rarelist[3][i] += self.word_tag_count[w][i]
                        rc[3] += 1
                        index = 3
            rf[index] += self.word_count[w]
            self.word_tag_count.pop(w)
                self.word_count.pop(w)
        rtags=['ALLCAPS','NUM','FLOAT','RARE']
        for i in range(4): 
            self.word_count[rtags[i]]=rf[i]
            self.word_tag_count[rtags[i]]=rarelist[i]
            print(rarelist[i])
            print("#rare words"+str(rc[i]))
        sorted_rw = sorted(self.__rare_word.items(), key=operator.itemgetter(1))
        sorted_rw.reverse()
        
        for k in range(100):
            print(str(sorted_rw[k])+"\n")
            
                      
        self.word_tag_prob = {}
        for w in self.word_tag_count.keys():
            self.word_tag_prob[w] = [0 for i in range(tag_num)]
                for i in range(tag_num):
        
                    self.word_tag_prob[w][i] = self.word_tag_count[w][i] / (1+self.tag_uni_count[i])
        self.tag_trigram_prob = [[[0 for k in range(tag_num)] for j in range(tag_num)] for i in range(tag_num)]
        for i in range(tag_num):
            for j in range(tag_num):
                for k in range(tag_num):
                    # q(i|j,k) that is the order of the tags is j,k,i
                    self.tag_trigram_prob[i][j][k] =  (self.tag_trigram_count[j][k][i]+1) /( self.vocabsize+self.tag_bigram_count[k][i])
        
    def test(self, filename, tag_num):
        resf = open('res.txt','w')
        resf.close()
        lines = open(filename).readlines()
        
        test_sents = [Sentence(tag_num)]
        for i in range(len(lines)-1):
            line = lines[i].strip('\n')
            if len(line) > 0:
                if not (line in self.word_count.keys()):
                    matchObj1 = re.match(r'[A-Z-]+',line)
                    matchObj2 = re.match(r'\d+',line)
                    matchObj3 = re.match(r'[0-9]*[.][-]*[0-9]+',line)
                    
                    
                    if not (matchObj1 is None):
                        test_sents[-1].add_word("ALLCAPS")
                        print("ALLCAPS")
                    elif not (matchObj2 is None):
                        test_sents[-1].add_word("NUM")
                        print("NUM")
                    elif not (matchObj3 is None):
                        test_sents[-1].add_word("FLOAT")
                        print("FLOAT")
                    else:
                        test_sents[-1].add_word("RARE")
                        print("RARE")
           
                else:
                    test_sents[-1].add_word(line)
            if (line=="$"):
                
                test_sents.append(Sentence(tag_num))
        
         
        right_num = 0
        total_num = 0
        result_list = []
        for s in test_sents:
            right_num += s.Viterbi(self.word_tag_prob, self.tag_trigram_prob, result_list)
            total_num += len(s.word) - 1
        #print (right_num / total_num)
def main():
#run e. g. python HMM.py --f1 train_data.txt --f2 test_data.txt
    parser = OptionParser()
    parser.add_option("--f1", dest = "file1", help = "tagged training file" ,default = "train_data.txt")
    parser.add_option("--f2", dest = "file2", help = "untagged test file", default = "test_data.txt" )
    (options, args) = parser.parse_args()
    train = HMM(options.file1, options.file2, 14)
        cPickle.dump(train, open('hmm-model', 'w'))
        train.test(options.file2, 14)
        
if __name__ == '__main__':
    main()
        
