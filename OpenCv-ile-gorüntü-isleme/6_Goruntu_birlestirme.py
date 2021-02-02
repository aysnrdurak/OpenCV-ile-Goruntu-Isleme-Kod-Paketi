import cv2
import numpy as np
img = cv2.imread("p3.png")
cv2.imshow("Resmimiz", img)

# yatay birleştirme
yatay = np.hstack((img,img,img))
cv2.imshow("Horizontal", yatay)
cv2.waitKey(0)

# dikey birleştirme
dikey = np.vstack((img,img))
cv2.imshow("Vertical", dikey)
cv2.waitKey(0)