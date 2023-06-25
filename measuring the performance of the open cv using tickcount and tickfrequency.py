# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:45:10 2023

@author: d jashwanth sai
"""

img1 = cv2.imread('C:\\opencv\\krishna.jpeg')
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)