# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:35:32 2023

@author: d jashwanth sai


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:\\opencv\\noise.jpeg')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:\\opencv\\noise.jpeg')

blur = cv2.blur(img,(5,5))
blur2 = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
blurbilateral = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(blur),plt.title('blur')
plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(median),plt.title('medianblur')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur2),plt.title('gaussianBLur')
plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(blurbilateral),plt.title('bilateralblur')
plt.xticks([]), plt.yticks([])
plt.show()
