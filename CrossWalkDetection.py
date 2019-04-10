import cv2 # opencv 사용
import math
import numpy as np

class SW_Detector:
    image = 0
    processed_image = 0
    def __init__(self,image): # 클래스 생성자
        self.image = image
    def get_processed_image(self): # 이미지 처리된거
        return self.processed_image
    def detect_sw(image): # 실제로 검사
        pr_img = process_image(image)
        lines = hough_lines(pr_img,1,1*np.pi/180,200,50,80)#횡단보도 특징 검출
        exist = check_cw(lines)
        return exist
    def roi(self, image, vertices): # 영역 설정
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, vertices, 255)
        masked = cv2.bitwise_and(image, mask)
        return masked
    def process_image(self): #이미지 가공처리
        #convert to gray
        processed_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        #edge detection
        processed_image = cv2.Canny(processed_image, threshold1 = 200, threshold2=300) # 경계값 설정 흰색선으로 하는게 좋을 듯
        #roi
        height , width , channel = self.image.shape
        vertices = np.array([[10,(height/3)*2],[width/4,height/3],[(width/4)*3,height/3],[width-10,(height/3)*2],], np.int32)
        processed_image = self.roi(processed_image, [vertices])
        self.processed_image = processed_image
    def check_rectangle(self): #사각형을 통해서 검출
        _, contours ,_ = cv2.findContours(self.processed_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        count = 0
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            #area = contours[count]
            #print(x,y)
            if len(approx) == 4:
                count+=1

        if count>=5:
            return True
        else:
            return False
    def check_cw(lines): # 라인을 통해 특징 검출하기
        result = False
        return result
    #minLineLength = 이 값 이하로 주어진 선 길이는 제외
    #maxLineGap = 찾은 직선이 이 값 이상 떨어져 있으면 다른 직선으로 간주
image = cv2.imread('c:\CrossWalk.bmp') # 이미지 읽기
processor = SW_Detector(image)
processor.process_image()
cw_check = processor.check_rectangle()
if cw_check:
    print("Exist SW")
else:
    print("Not Exist SW")
#processor.hough_lines(1,1*np.pi/180,50,10,50)
mark = processor.get_processed_image()

cv2.imshow('result',mark) # 이미지 출력
cv2.waitKey(0)
