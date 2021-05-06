import cv2
import numpy as np

def getContor(img):
    contor ,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contor:
        peri = cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,0.02*peri,True)
        print(peri)
        print(approx)
        obj= len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(imgContor,(x,y),(x+w,y+h),(0,0,255),3)
        if obj==3: objType="Tri"
        elif obj == 4:
            aspRatio=w/float(h)
            if aspRatio >0.95 and aspRatio < 1.05:objType= "square"
            else: objType = "rect"
        elif obj>4: objType="circle"
        else:objType="None"
        cv2.putText(imgContor,objType,((x+w//2)-10,(y+h//2)-10),cv2.FONT_ITALIC,0.5,(0,0,0),2)

path ="Resource/shapes.png"
img = cv2.imread(path)
imgContor= img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContor(imgCanny)




cv2.imshow("output", img)
cv2.imshow("output_Gray", imgGray)
cv2.imshow("output_Blur", imgBlur)
cv2.imshow("output_Canny", imgCanny)
cv2.imshow("output_Conyor", imgContor)


cv2.waitKey(0)

