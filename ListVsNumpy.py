import numpy as np
from time import time


def pythonVersion():
    t1 = time()
    x = range(100_000_000)
    y = range(100_000_000)
    z = []
    for i in range(100_000_000):
        z.append(x[i] + y[i])
    t2 = time()
    return t2 - t1


def numpyVersion():
    t1 = time()
    x = np.arange(100_000_000)
    y = np.arange(100_000_000)
    z = x + y
    t2 = time()
    return t2 - t1


print(f'time for python : {pythonVersion()}')
print(f'time for numpy : {numpyVersion()}')
