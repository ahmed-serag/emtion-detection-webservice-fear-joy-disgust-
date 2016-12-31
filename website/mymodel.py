from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy
from cProfile import run
from nltk.corpus import stopwords



print('init hi')
model = load_model('my_model.h5')

