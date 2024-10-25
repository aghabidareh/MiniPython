import numpy as np

sequnce = np.array([1 , 2])

s = 0

for i in range(50):
    sequnce = np.append(sequnce, sequnce[-2] + sequnce[-1])

sequnce = sequnce[sequnce % 2 == 0]
sequnce = sequnce[sequnce < 4_000_000]
s = np.sum(sequnce)

print(s)