#!/usr/bin/env python

# for ptvsd debug.
import ptvsd
import platform

import cv2
import numpy as np

# for ptvsd debug.
ptvsd.enable_attach(secret = 'ptvsd')
os = platform.system()
print 'Waiting for attach...'
if os != 'Windows':
    ptvsd.wait_for_attach()


filename = 'simple.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
# uses Harris algorithm to detect corners
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

# display result.
cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

