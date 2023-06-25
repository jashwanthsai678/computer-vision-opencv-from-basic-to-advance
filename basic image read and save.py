# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 21:48:11 2023

@author: d jashwanth sai
"""

import numpy as np
import cv2
img = cv2.imread('C:\\opencv\\ss0krishna.jpeg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
