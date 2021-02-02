import cv2
import numpy as np
img = cv2.imread("kart.png")
cv2.imshow("Orijinal", img)
cv2.waitKey(0)

width = 400
height = 500

# resmimizin köşelerinin piksel değerlerini bilmeliyiz
# paint kullanarak bu değerleri elde edebiliriz

# çevirmek istediğim resmimin köşeleri:
pts1 = np.float32([[206,4],[1,468], [537,150], [337,614]])
# istediğimiz hali:
pts2 = np.float32([[0,0], [0, height], [width, 0], [height,width]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Donusturulmus", imgOutput)
cv2.waitKey(0)