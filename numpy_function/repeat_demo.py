import numpy as np

i = np.arange(10)

print 'i -->', i

a = np.array([1,2,3,4,5,6])

print 'a -->', a

r = np.repeat(i, 5)
print 'r -->', r

cut = r[:, np.newaxis]

print 'c -->', cut
print 'np.newaxis -->', np.newaxis
