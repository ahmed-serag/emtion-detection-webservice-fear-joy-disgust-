from django.shortcuts import render
from django.http import HttpResponse


from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy
from cProfile import run
from sentence import sentence
from nltk.corpus import stopwords

def stop_words_remove(text):
        cachedStopWords = stopwords.words("english")
        text = ' '.join([word for word in text.split() if word not in cachedStopWords])    
        return text
 

run = 0
  
def getemoj(request):
   
    global run
  
    run = run + 1 
    text = request.GET['sentence']
    line = stop_words_remove(text)
    sent = sentence(line,'NONE')
    sent.init_sent_vector()


    X = numpy.asarray([sent.get_sentence_vector()])   
    
    getemoj.model = load_model('my_model.h5')
    
    predictions = getemoj.model.predict(X)
     
    
    feels =predictions.tolist()

    f = feels[0]
    ind = f.index(max(f))
   
    if(ind == 0):
        response = "you are feeling really afraid?! why so serious?"
    elif (ind == 1):
        response = "you are feeling really disgusting"
    else:
        response = "you are feeling happy that's awesome"
    
   
    return HttpResponse(response)





# Create your views here.




