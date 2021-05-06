import cv2

img =cv2.imread("Resource/try2.jpg")
print(img.shape)
imgResize = cv2.resize(img,(150,150))
cv2.imshow("output",img)
cv2.imshow("output_resize",imgResize)
cv2.waitKey(0)
