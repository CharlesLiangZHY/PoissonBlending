import sys
import cv2 as cv
import numpy as np

import poisson

if __name__ == "__main__":
    folder = None
    mixing = False # mixing gradient flag
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-f':
            folder = sys.argv[i+1]
        if sys.argv[i] == "-m":
            mixing = True

    ### images have been trimmed and aligned
    src  = cv.imread("img/"+ folder +"/"+ "src.jpg")
    dst  = cv.imread("img/"+ folder +"/"+ "dst.jpg")
    mask = cv.imread("img/"+ folder +"/"+ "mask.jpg")

    index_map, coordinate_map = poisson.map_Omega(src, dst, mask)
    A,b = poisson.construct_DPE(src, dst, mask, index_map, coordinate_map, mixing)
    xr, xg, xb = poisson.solve_DPE(A,b)

    # generate the image
    for i in range(len(xr)):
        y,x = coordinate_map[i]
        dst[y,x,0] = np.clip(xr[i],0,255) # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.clip.html
        dst[y,x,1] = np.clip(xg[i],0,255)
        dst[y,x,2] = np.clip(xb[i],0,255)

    cv.imwrite("img/"+ folder +"/"+ folder +"_result.jpg", dst)

