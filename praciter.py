
import numpy as np

x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

mx = np.mean(x)
my = np.mean(y)

divisor = sum([(i-mx)]**2 for i in x)