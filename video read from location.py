# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 21:59:01 2023

@author: d jashwanth sai
"""

import numpy as np
import cv2
cap = cv2.VideoCapture('video location')
while(cap.isOpened()):
     ret, frame = cap.read()
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     cv2.imshow('frame',gray)
     if cv2.waitKey(1) & 0xFF == ord('q'):
     break
cap.release()
cv2.destroyAllWindows()