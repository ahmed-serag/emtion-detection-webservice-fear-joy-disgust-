from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy

dataset = numpy.loadtxt("dataset.txt", delimiter=",")
# split into input (X) and output (Y) variables
#Train Set
X = dataset[0:1500,0:170]

X2 = dataset[600:,0:170]
y2_int = dataset[600:,170]
Y2 = to_categorical(y2_int)

y_int = dataset[0:1500,170:]
Y = to_categorical(y_int)
#Test Set


X2Test = dataset[:600,0:170]
y2test_int = dataset[:600,170]
y2Test = to_categorical(y2test_int)



XTest = dataset[1500:,0:170]
ytest_int = dataset[1500:,170:]
yTest = to_categorical(ytest_int)
# create model
model = Sequential()
model.add(Dense(125, input_dim=170, init='uniform', activation='relu'))

model.add(Dense(50, init='uniform', activation='relu'))
model.add(Dense(25, init='uniform', activation='relu'))
model.add(Dense(5, init='uniform', activation='relu'))
model.add(Dense(3, init='uniform', activation='softmax'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, y_int, nb_epoch=5000, batch_size=10)
model.fit(X2, Y2, nb_epoch=5000, batch_size=10)
# evaluate the model

scores = model.evaluate(XTest, ytest_int)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
predictions = model.predict(X)
print(predictions)
rounded= numpy.around(predictions, decimals=0)
print(rounded)

model.save('my_model.h5')

