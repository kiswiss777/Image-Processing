import numpy as np
import cv2

def contour():#사각형 검출
    img = cv2.imread('c:\CrossWalk.bmp')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret , thr = cv2.threshold(imgray,200,255,0)
    thr = cv2.GaussianBlur(thr,(5,5),0)
    _, contours ,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) == 4:
            count+=1
    print(count)
    cv2.drawContours(img, contours,-1,(0,0,255),1)
    cv2.imshow('thresh',thr)
    cv2.imshow('contour',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()
