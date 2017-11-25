import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
b = np.array([1,2,3,4,6,6,7,8])

matches = a == b

print matches

print np.count_nonzero(matches)
