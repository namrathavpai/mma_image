import cv2
import numpy as np

# def empty(a):
#     pass

cap= cv2.VideoCapture(0)
cap.set(3,640)#set width
cap.set(4,480)#set height
cap.set(10,100)

# cv2.namedWindow("TaskBar1")
# cv2.resizeWindow("TaskBar1",640,240)
# cv2.createTrackbar("Hue min","TaskBar1",0,179,empty)
# cv2.createTrackbar("Hue max","TaskBar1",179,179,empty)
# cv2.createTrackbar("Sat min","TaskBar1",0,255,empty)
# cv2.createTrackbar("Sat max","TaskBar1",255,255,empty)
# cv2.createTrackbar("Val min","TaskBar1",0,255,empty)
# cv2.createTrackbar("Val max","TaskBar1",255,255,empty)

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("hue min ","TrackBars",2,179,empty)
# cv2.createTrackbar("hue max ","TrackBars",13,179,empty)
# cv2.createTrackbar("saturation min ","TrackBars",54,255,empty)
# cv2.createTrackbar("saturation max ","TrackBars",255,255,empty)
# cv2.createTrackbar("val min ","TrackBars",58,255,empty)
# cv2.createTrackbar("val max ","TrackBars",255,255,empty)


myColors=[[99,175,37,128,255,83],
           [17,57,67,45,125,210]]

def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for clr in myColors:
        lower = np.array(clr[0:3])
        upper = np.array(clr[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getContor(mask)
        cv2.circle(imgResult,(x,y),5,(0,255,255),2)
        #cv2.imshow(str(clr[0]), mask)

def getContor(img):
    x,y,h,w=0,0,0,0
    contor ,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contor:
        cv2.drawContours(imgResult,cnt,-1,(255,0,0),2)
        peri = cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,0.02*peri,True)
        x, y, w, h = cv2.boundingRect(approx)
    return  x+w//2,y


while True:
    success , img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgResult = img.copy()
    # h_min = cv2.getTrackbarPos("Hue min","TaskBar1")
    # h_max = cv2.getTrackbarPos("Hue max","TaskBar1")
    # s_min = cv2.getTrackbarPos("Sat min","TaskBar1")
    # s_max = cv2.getTrackbarPos("Sat max","TaskBar1")
    # v_min = cv2.getTrackbarPos("Val min","TaskBar1")
    # v_max = cv2.getTrackbarPos("Val max","TaskBar1")
    # lower = np.array([h_min, s_min, v_min])
    # upper = np.array([h_max, s_max, v_max])
    # mask = cv2.inRange(imgHSV, lower, upper)
    findColor(img)
    # imgResult = cv2.bitwise_and(img, img, mask=mask)
    # mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow("out",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("mask", mask)
    cv2.imshow("RESULT", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break


