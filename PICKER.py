import cv2
import numpy as np

def empty(a):
    pass

cap= cv2.VideoCapture(0)
cap.set(3,640)#set width
cap.set(4,480)#set height
cap.set(10,100)

cv2.namedWindow("TaskBar1")
cv2.resizeWindow("TaskBar1",640,240)
cv2.createTrackbar("Hue min","TaskBar1",0,179,empty)
cv2.createTrackbar("Hue max","TaskBar1",179,179,empty)
cv2.createTrackbar("Sat min","TaskBar1",0,255,empty)
cv2.createTrackbar("Sat max","TaskBar1",255,255,empty)
cv2.createTrackbar("Val min","TaskBar1",0,255,empty)
cv2.createTrackbar("Val max","TaskBar1",255,255,empty)

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("hue min ","TrackBars",2,179,empty)
# cv2.createTrackbar("hue max ","TrackBars",13,179,empty)
# cv2.createTrackbar("saturation min ","TrackBars",54,255,empty)
# cv2.createTrackbar("saturation max ","TrackBars",255,255,empty)
# cv2.createTrackbar("val min ","TrackBars",58,255,empty)
# cv2.createTrackbar("val max ","TrackBars",255,255,empty)



# def findColor(img):
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imgHSV, lower, upper)
#     cv2.imshow("mask", mask)




while True:
    success , img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min","TaskBar1")
    h_max = cv2.getTrackbarPos("Hue max","TaskBar1")
    s_min = cv2.getTrackbarPos("Sat min","TaskBar1")
    s_max = cv2.getTrackbarPos("Sat max","TaskBar1")
    v_min = cv2.getTrackbarPos("Val min","TaskBar1")
    v_max = cv2.getTrackbarPos("Val max","TaskBar1")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow("out",img)
    #cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("RESULT", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break


