import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#img[:]= 255,0,0  #convert into blue colour

cv2.line(img,(0,0),(300,300),(0,255,255),3) #drawing line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3) #drawing line

cv2.rectangle(img,(0,0),(200,200),(0,255,255),3)# drawing triangle
cv2.rectangle(img,(0,0),(200,200),(0,255,255),cv2.FILLED)#filling a triangle

cv2.circle(img,(500,400),30,(255,255,0),5)#draw circle

cv2.putText(img,"try this text",(200,400),cv2.FONT_ITALIC,1,(0,150,255),1) #putting text

cv2.imshow("output", img)
cv2.waitKey(0)