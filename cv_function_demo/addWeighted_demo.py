import cv2
import numpy as np

img1 = cv2.imread('../../sample_data/image/apple.png')
img2 = cv2.imread('../../sample_data/image/logo.png')

img11 = img1[0:50, 0:50] # ROI
img22 = img2[0:50, 0:50] # ROI


img3 = cv2.addWeighted(img11, 0.6, img22, 0.4, 0) 
img4 = cv2.addWeighted(img11, 0.8, img22, 0.2, 0) 

cv2.imshow('Origin Apple', img1)
cv2.imshow('Origin Logo', img2)
cv2.imshow('%60 Apple | %40 Logo', img3)
cv2.imshow('%80 Apple | %20 Logo', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
