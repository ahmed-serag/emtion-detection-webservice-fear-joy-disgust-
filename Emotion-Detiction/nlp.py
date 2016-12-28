'''
Created on Dec 20, 2016

@author: Ahmed Sirage
'''
from nltk.corpus import stopwords
from sentence import sentence
from random import randint
'''
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical

import numpy
from numpy.random import random
'''




'''
glopal variables
'''
joy_sentences = []
fear_sentences = []
disgust_sentences = []
sentences = []

def stop_words_remove(text):
        cachedStopWords = stopwords.words("english")
        text = ' '.join([word for word in text.split() if word not in cachedStopWords])    
        return text
   
def init_joy():
    global sentences
    joy_file = open('joyToken.txt','r')
    for line in joy_file:
        line = stop_words_remove(line)
        sentences.append(sentence(line,'joy'))
    joy_file.close()
       
def init_fear():
    global sentences
    fear_file = open('fearToken.txt','r')
    for line in fear_file:
        line = stop_words_remove(line)
        sentences.append(sentence(line,'fear'))
    fear_file.close()
    
def init_disgust():
    global sentences
    disgust_file = open('DisgustToken.txt','r')
    for line in disgust_file:
        line = stop_words_remove(line)
        sentences.append(sentence(line,'disgust'))
    disgust_file.close()
    
    
if __name__ == '__main__':
    
    init_joy()
    init_fear()
    init_disgust()
    
    for sent in sentences:
        sent.init_sent_vector()
    for i in range(len(sentences)-1):
        rand = randint(0, len(sentences)-1)
        b = sentences[i]
        sentences[i] = sentences[rand]
        sentences[rand] = b
            
            
    print('maximum Sentence length: '+sentence.length)
    x = []
    y = []
    f = open('dataset.txt','w')
    for sent in sentences:
        instance = sent.get_sentence_vector()
        if sent.get_emoj() == ('joy'):
            
            st = ','.join(str(v) for v in instance)
            f.write(st)
            f.write(',0,0,1')
       
        elif sent.get_emoj() == ('fear'):
            st = ','.join(str(v) for v in instance)
            f.write(st)
            f.write(',1,0,0')
        else:
            st = ','.join(str(v) for v in instance)
            f.write(st)
            f.write(',0,1,0')
          
        f.write('\n')
   
    f.close()
