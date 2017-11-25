import cv2
import numpy as np

# imread(filename[, flags]) -> retval
image = cv2.imread('../../sample_data/image/apple.png')

print image.shape
