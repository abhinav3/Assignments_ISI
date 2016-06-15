#!/usr/bin/env python3
from __future__ import division
from math import log
class Sentence:
    '''
    classdocs
    '''

    def __init__(self, tag_num):
        '''
        Constructor
        '''
        self.word_tag = []
        '''map of word tag'''
        self.tag_num = tag_num
        '''{'NUM': 6664, '.': 71555, 'X': 590, 'VERB': 89766, 'DET': 63164,
'NOUN': 120770, 'CONJ': 17779, 'PRT': 15622, 'ADP': 65861, 'ADV': 27683, 'PRON': 27229, 'ADJ': 36466}
12
'''
        self.tag_dict = {'NUM' : 0, 'X' : 1, 'VERB' : 2, 'DET' : 3, 'NOUN':4, 'CONJ':5, 'PRT':6, 'ADP':7,'ADV':8,'PRON':9,'ADJ':10,'.':11,'$':12,'*':13}
        self.tag_dict_rev = ['NUM', 'X', 'VERB', 'DET', 'NOUN','CONJ', 'PRT', 'ADP','ADV','PRON','ADJ','.','$','*']
        
    	self.word=[]
    def add_word_tag(self, word, tag):
        self.word_tag.append((word, tag))
    
    def add_word(self, word):
        self.word.append(word)
        
        
    def finish(self, word_dict, word_tag_dict, tag_uni_count, tag_bigram_count, tag_trigram_count):
        #self.add_word_tag('$', '$')
        self.cal_word_tag_count(word_tag_dict)
        '''for now empty hai'''
        self.cal_tag_uni_count(tag_uni_count)
        self.cal_tag_bigram_count(tag_bigram_count)
        self.cal_tag_trigram_count(tag_trigram_count)
        self.cal_word_count(word_dict)
        #print(" ENDl ")
        #print(self.word_tag)
    	
    def cal_word_count(self, word_dict):
        '''calculate no. of unique words in the corpus'''
        for i in range(len(self.word_tag)):
            if self.word_tag[i][0] in word_dict:
                word_dict[self.word_tag[i][0]] += 1
            else:
                word_dict[self.word_tag[i][0]] = 1
    
    def cal_word_tag_count(self, word_tag_dict):
        '''word-tag unique counts aa: A-2 B-3 C-4 D-0'''
        for i in range( len(self.word_tag)):
            if self.word_tag[i][0] not in word_tag_dict:
                word_tag_dict[self.word_tag[i][0]] = [0 for j in range(self.tag_num)]
            word_tag_dict[self.word_tag[i][0]][self.tag_dict[self.word_tag[i][1]]] += 1
    
    def cal_tag_uni_count(self, tag_uni_count):
        '''calculate freq of each tag'''
        for i in range(len(self.word_tag)):
            tag_uni_count[self.tag_dict[self.word_tag[i][1]]] += 1
        
    def cal_tag_bigram_count(self, tag_bigram_count):
        '''limitation: sentence boundary not taken care of. entire corpus pair shift by one and see next pair'''
        for i in range(1, len(self.word_tag) - 1):
            tag_bigram_count[self.tag_dict[self.word_tag[i][1]]][self.tag_dict[self.word_tag[i + 1][1]]] += 1
                
    def cal_tag_trigram_count(self, tag_trigram_count):
        for i in range( len(self.word_tag) - 2):
            tag_trigram_count[self.tag_dict[self.word_tag[i][1]]][self.tag_dict[self.word_tag[i + 1][1]]][self.tag_dict[self.word_tag[i + 2][1]]] +=1
    
    def Viterbi(self, word_tag_prob, tag_trigram_prob, result_list):
       # print("INVITERBI ")
        #print(self.word)
        Pi[0][self.tag_dict['*']][self.tag_dict['*']] = (1,13)
                       
        for k in range(1, len(self.word)):
            for u in range(self.tag_num):
                for v in range(self.tag_num):
                    for w in range(self.tag_num):
                    	#print (Pi[k-1][w][u])
                    	#print (Pi[k-1][w][u][1])
                    	#tem_prob=0.12
                        tem_prob = (Pi[k-1 ][w][u][0]) * tag_trigram_prob[v][w][u] * word_tag_prob[self.word[k]][v]
                       # print (k,u,v)
                        #Pi[k][u][v]=(9,9)
                        if tem_prob > Pi[k][u][v][0]:
                            Pi[k][u][v] = (tem_prob,w)
                            #Pi[k][u][v][1] = w
        
        result = []
        max_pos = (0, 0)
        max_value = 0
        for j in range(self.tag_num):
            for k in range(self.tag_num):
                if max_value < Pi[-1][j][k][0]:
                    max_pos = (j, k)
                    max_value = Pi[-1][j][k][0]
       # print("length of PI %d", len(Pi))
        for i in range(len(Pi) - 1, 0, -1):
            #if(self._rare_word(word[i]) == None):
            max_pos = (Pi[i][max_pos[0]][max_pos[1]][1], max_pos[0])
            result.append(self.tag_dict_rev[max_pos[1]])
            
        # result.append('B')
        result.reverse()
        right_num = 1
        res = open("res.txt","a+")
        for i in range(len(self.word) - 1):
            res.write(''.join(self.word[i]))
            
            res.write("/"+result[i]+"\n")
            result_list.append(result[i])
            #if result[i] == self.word_tag[i][1]:
                #right_num += 1
        result_list.append('$')
        res.write("$/$\n")
        return right_num
