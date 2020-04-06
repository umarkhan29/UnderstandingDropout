import tensorflow as tf
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.optimizers import Adam
import numpy as np

print("TF Version")
print(tf.__version__)


#Generating Training Data
number = []
squares = []

for x in range(14):
  num = x
  square = num * num
  number.append(num)
  squares.append(square)


#Defining Model
model = Sequential()
model.add(Dense(1,input_shape = (1,)))

#adding dropout layer
model.add(Dropout(0.25, noise_shape=None, seed=None))


#Compiling Model
model.compile(loss='mean_squared_error', optimizer=Adam(0.1), metrics=['accuracy'])

#Training Model
history = model.fit(number, squares, epochs=700, verbose=0)


# save model and architecture to single file
model.save("dr-square-model.h5")
print("Model Saved !")
