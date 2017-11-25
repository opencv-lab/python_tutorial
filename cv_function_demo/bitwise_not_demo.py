import cv2
import numpy as np

img = cv2.imread('../../sample_data/image/apple.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#  bitwise_not(src[, dst[, mask]]) -> dst
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
