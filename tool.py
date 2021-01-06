import cv2 as cv
import numpy as np

import sys

### to ensure all pixels are either 255 or 0
def trim(path):
	img = cv.imread(path)
	w,h,_ = img.shape
	grey = np.mean(img, axis=2)
	for i in range(w):
		for j in range(h):
			if grey[i,j] >= 20:
				img[i,j,:] = 255
			else:
				img[i,j,:] = 0
	cv.imwrite(path,img)



if __name__ == "__main__":
	trim(sys.argv[1])