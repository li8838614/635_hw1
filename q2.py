from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions

df=pd.read_csv("./Data/Frogs-subsample.csv")
#0 for HylaMinuta, 1 for HypsiboasCinerascens
df.Species[df.Species == 'HylaMinuta'] = 0.0
df.Species[df.Species == 'HypsiboasCinerascens'] = 1.0

X = df.drop(['Species'], axis=1)
X=X.to_numpy(dtype=np.float)
Y = df['Species']
Y=Y.to_numpy(dtype=np.float)

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
#print(X_train)

model = Sequential()
model.add(Dense(1,activation = 'sigmoid',input_dim = 2))
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x=X, y=Y, epochs=100)
prediction=model.predict(X)
plot_decision_regions(X=X, y=Y.astype(np.int_),clf=model,legend=2)
plt.title("sigmoid_percepton_subsample_decision")
plt.show()


df=pd.read_csv("./Data/Frogs.csv")
#0 for HylaMinuta, 1 for HypsiboasCinerascens
df.Species[df.Species == 'HylaMinuta'] = 0.0
df.Species[df.Species == 'HypsiboasCinerascens'] = 1.0

X = df.drop(['Species'], axis=1)
X=X.to_numpy(dtype=np.float)
Y = df['Species']
Y=Y.to_numpy(dtype=np.float)

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
#print(X_train)

model = Sequential()
model.add(Dense(1,activation = 'sigmoid',input_dim = 2))
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(x=X, y=Y, epochs=100, batch_size=25, validation_split=0.2)
prediction=model.predict(X)
plot_decision_regions(X=X, y=Y.astype(np.int_),clf=model,legend=2)
plt.title("sigmoid_percepton_Frogs_decision")
plt.show()