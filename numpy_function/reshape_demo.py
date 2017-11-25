import numpy as np

npaClassifications = np.loadtxt("../../sample_data/txt/plate_train.txt")

print "Origin data -->", npaClassifications

print "Reshape data -->", npaClassifications.reshape(npaClassifications.size, 1)
print "Reshape data -->", npaClassifications.reshape(npaClassifications.size/2, 2)
