import cv2 # opencv 사용
import numpy as np

def roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked

def process_image(image_array):
    #convert to gray
    processed_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    #edge detection
    processed_image = cv2.Canny(processed_image, threshold1 = 200, threshold2=300) # 경계값 설정 흰색선으로 하는게 좋을 듯
    #roi
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],], np.int32)#영역설정
    processed_image = roi(processed_image, [vertices])
    return processed_image

image = cv2.imread('c:\lineTest.bmp') # 이미지 읽기
mark = process_image(image);

cv2.imshow('roi_white',mark) # 흰색 차선 추출 결과 출력
cv2.imshow('result',image) # 이미지 출력
cv2.waitKey(0)
