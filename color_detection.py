import cv2
import numpy as np

def empty(q):
    pass

path ="Resource/try3.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("hue min ","TrackBars",2,179,empty)
cv2.createTrackbar("hue max ","TrackBars",13,179,empty)
cv2.createTrackbar("saturation min ","TrackBars",54,255,empty)
cv2.createTrackbar("saturation max ","TrackBars",255,255,empty)
cv2.createTrackbar("val min ","TrackBars",58,255,empty)
cv2.createTrackbar("val max ","TrackBars",255,255,empty)

cap = cv2.VideoCapture(0)
cap.set(3,640)#set width
cap.set(4,480)#set height
cap.set(10,100)

while True:
    _,imgHSV1= cap.read()
    imgHSV = cv2.cvtColor(imgHSV1,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min ","TrackBars")
    h_max = cv2.getTrackbarPos("hue max ", "TrackBars")
    s_min = cv2.getTrackbarPos("saturation min ", "TrackBars")
    s_max = cv2.getTrackbarPos("saturation max ", "TrackBars")
    v_min = cv2.getTrackbarPos("val min ", "TrackBars")
    v_max = cv2.getTrackbarPos("val max ", "TrackBars")
    lower = np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(imgHSV1, imgHSV1, mask=mask)


    cv2.imshow("out",imgHSV1)
    cv2.imshow("outHSV",imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("imgResult", imgResult)
    cv2.waitKey(1)