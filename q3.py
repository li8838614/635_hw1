from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions

dataset=np.load("Hastie-data.npy")
X=dataset[:,:-1]
Y=dataset[:,-1]
print(X)



#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
#print(X_train)

model = Sequential()
model.add(Dense(100,activation = 'relu',input_dim = 2))
model.add(Dense(1,activation = 'sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x=X, y=Y, epochs=500, batch_size=25, validation_split=0.2)
#prediction=model.predict(X_test)
plot_decision_regions(X=X, y=Y.astype(np.int_),clf=model,legend=2)
plt.title("neural_net_Hastie_decision")
plt.show()