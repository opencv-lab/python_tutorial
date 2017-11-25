import cv2
import numpy as np

# It's hard to find a ROI, so try to build a tool!
img = cv2.imread('../../sample_data/image/plate.jpg')

roi = img[140:380, 130:800]

cv2.imshow('Origin Image', img)
cv2.imshow('Certain ROI', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
