import cv2
import numpy as np

img = cv2.imread('../../sample_data/image/apple.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold(src, thresh, maxval, type[, dst]) -> retval, dst
ret, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('gray', gray)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
