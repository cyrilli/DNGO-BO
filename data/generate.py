from data.func import obj
import numpy as np

X = [-1, 2, 4, -5, 1.5]
Y = []

for x in X:
    Y.append(obj(x))

X = np.array(X)
X = np.expand_dims(X, axis=1)
Y = np.array(Y)

np.save("X.npy", X)
np.save("y.npy", Y)

X = np.load("X.npy")
print(X)

Y = np.load("y.npy")
print(Y)