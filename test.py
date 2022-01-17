import numpy as np
import imageio
import scipy.ndimage

import cv2
def rgb2gray(a):
    return np.dot(a[...,:3],[0.2989,0.5870,0.1140])

def dodge(front , back):
    final_sketch = front*255/(255-back)
    #final_sketch[final_sketch>255]=255
    #final_sketch[back==255]=255
    return final_sketch.astype('uint8')


ss = imageio.imread("megha.jpg")

gray=rgb2gray(ss)
i=255-gray

#to convert into blur image
blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)

#sigma is the intensity of the blurness of the image

#this function will convert our image to sketch by taking two parameter as blur and gray

r = dodge(blur , gray)

cv2.imwrite("dummy-sketch.jpg",r    )
