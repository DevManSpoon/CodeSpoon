
from keras.models import Sequential
from keras.layers import Dense
import numpy

#random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# datasets, input and output
dset = numpy.loadtxt("trends.csv", delimiter=",")
X = dset[:,0:8]
Y = dset[:,8]

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='motion', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=150, batch_size=10,  verbose=2)

# calculate predictions
predictions = model.predict(X)

# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
