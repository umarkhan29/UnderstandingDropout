from keras.models import load_model
 
# load model
model = load_model('dr-square-model.h5')


#enter number to predict
print("Enter Number: ")
num = input()
num=[num]

#Predicting a sample
print(model.predict([num]))