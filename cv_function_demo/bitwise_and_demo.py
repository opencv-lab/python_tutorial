import cv2
import numpy as np

img = cv2.imread('../../sample_data/image/apple.png')

roi = img[30:80, 30:80]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#  bitwise_not(src[, dst[, mask]]) -> dst
mask_inv = cv2.bitwise_not(mask)
new_roi = cv2.bitwise_and(roi, roi, mask=mask_inv)
img_fg = cv2.bitwise_and(img, img, mask=mask)

#dst = cv2.add(new_roi, img_fg)

cv2.imshow('image fg', img_fg)
#cv2.imshow('add two image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
