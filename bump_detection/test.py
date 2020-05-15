import numpy as np

Y = np.arange(16).reshape(4, 4)
print(Y)
print(Y[np.ix_([0], [0, 3])])


print( np.zeros((32, 1)) )