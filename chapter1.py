import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
#imported opev cv


# #for image
# img =cv2.imread("Resource/try.jpg")
# cv2.imshow("out",img)
# cv2.waitKey(0)


# for vedio
# cap = cv2.VideoCapture("Resource/vedio.mp4")
# #to show image use while loop as the video is the sequence of images
# while True:
#     success ,  img = cap.read()
#     cv2.imshow("out",img)
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break


# # use web cam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)#set width
# cap.set(4,480)#set height
# cap.set(10,100)
#
# while True:
#     success ,  img = cap.read()
#     cv2.imshow("out",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

img = cv2.imread("Resource/try.jpg")
print(img.shape)
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# convert image tp grey scale
ingBlur = cv2.GaussianBlur(imgGrey,(7,7),0)#blur image
imgCanny = cv2.Canny(img,200,50)#edge detection
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #diate the edges in the images
imgErode =cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("out",imgGrey)
cv2.imshow("out_blur",ingBlur)
cv2.imshow("out_canny",imgCanny)
cv2.imshow("out_dialate",imgDialation)
cv2.imshow("out_erode",imgErode)
cv2.waitKey(0)