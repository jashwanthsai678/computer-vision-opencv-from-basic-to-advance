# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:40:09 2023

@author: d jashwanth sai
"""
import cv2 
import numpy as np


img1 = cv2.imread('image 1 location')
img2 = cv2.imread('image 2 location')
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()