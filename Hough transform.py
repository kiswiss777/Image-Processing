import cv2
import sys
import math
import numpy as np


image = cv2.imread('c:\lineTest.bmp')
height, width = image.shape[:2] # 이미지 높이, 너비
gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray_image,50,150,apertureSize=3)

lines = cv2.HoughLines(edges,1,np.pi/180,140)

for line in lines:
    r,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*r
    y0 = b*r
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*a)
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*a)

    cv2.line(image,(x1,y1),(x2,y2),(0,0,255),1)

cv2.imshow('result',image)
cv2.waitKey(0)
