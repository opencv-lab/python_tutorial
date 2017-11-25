import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../sample_data/image/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we split the imgae to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# Make it into a Numpy array. It size will be (50, 100, 20, 20)
x = np.array(cells)


for i in range(0, 50, 5):
    cv2.imshow('number --> {}'.format(divmod(i, 5)), x[i][0])
    print x[i][0]
cv2.waitKey(0)
cv2.destroyAllWindows()
