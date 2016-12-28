'''
Created on Dec 21, 2016

@author: Ahmed Sirage
'''
from nltk import SnowballStemmer
from tensorflow.python.framework.tensor_shape import vector
from nltk import word_tokenize


def get_line_stem(word):
    s = SnowballStemmer("english")
    return s.stem(word)


def init_lexicon_dictionary():
    lexicon_dictionary = {} 
    lexicon_stemmed_dictionary = {}
    ld_file = open('lexicon_dictionary.txt','r')
    for line in ld_file:
        word = line[:-22]
        vector = line[-21:-2].split()
        lexicon_dictionary[word] = vector
        lexicon_stemmed_dictionary[get_line_stem(word)] = vector
    ld_file.close()
    
    return lexicon_dictionary, lexicon_stemmed_dictionary


class sentence:
    '''
    classdocs
    ''' 
    lexicon_dictionary, lexicon_stemmed_dictionary = init_lexicon_dictionary()
    length = 0
    bayz=0
    kolo=0

    def __init__(self, text,emoj):
        '''
        Constructor
        '''
        self.text = text
        self.emoj = emoj
        self.words = {}
        self.tokens = word_tokenize(text, "english")


        for word in self.tokens:
            if word.lower() in sentence.lexicon_dictionary:
                if '1' in sentence.lexicon_dictionary[word.lower()]:
                    self.words[word.lower()] = sentence.lexicon_dictionary[word.lower()]
            elif word.lower() in sentence.lexicon_stemmed_dictionary:
                if '1' in sentence.lexicon_stemmed_dictionary[word.lower()]:
                    self.words[word.lower()] = sentence.lexicon_stemmed_dictionary[word.lower()]
            else:
                word_stem = get_line_stem(word) 
                if word_stem.lower() in sentence.lexicon_dictionary:
                    if '1' in sentence.lexicon_dictionary[word_stem]:
                        self.words[word.lower()] = sentence.lexicon_dictionary[word_stem]
                elif word_stem.lower() in sentence.lexicon_stemmed_dictionary:
                    if '1' in sentence.lexicon_stemmed_dictionary[word_stem]:
                        self.words[word.lower()] = sentence.lexicon_stemmed_dictionary[word_stem]
               
        if len(self.words) > sentence.length:
            sentence.length = len(self.words)     
                    
                    
    def get_words(self):
        return self.words                
    
    def get_text(self):
        return self.text                
    
    def get_len(self):
        return sentence.length                
    
    
    def get_emoj(self):
        return self.emoj                
                    
    
    def init_sent_vector(self):
        self.vector=[]
        temp=[0,0,0,0,0,0,0,0,0,0]
        for word in self.words:
            for vec in self.words[word]:
                self.vector.append(int(vec))
        if len(self.vector) < (sentence.length*10):
            for i in range((sentence.length*10)-len(self.vector)):
                self.vector.append(0)
        for word in self.words:
            print(self.words[word])
            d=0
            for i in self.words[word]:
                if(temp[d] == 1 or i == '1'):
                    temp[d] = 1
                d=d+1
                
            
                              
        
        for i in temp:
            self.vector.append(i)
            
        print(temp)    
        
    def get_sentence_vector(self):
        return self.vector    
        
                    
                    
                    