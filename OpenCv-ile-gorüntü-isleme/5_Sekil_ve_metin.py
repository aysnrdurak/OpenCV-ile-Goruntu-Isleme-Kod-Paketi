import cv2
import numpy as np 

# resim oluşturmak

img = np.zeros((512,512,3), np.uint8) # siyah bir resim
print(img.shape)

cv2.imshow("Siyah", img)
cv2.waitKey(0)

# çizgi
# parantez içi sıralama şu şekildedir: 
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
# renk OpenCV'de BGR şeklindedir.
cv2.line(img, (0,0),(512,512), (0,255,0), 3)
cv2.line(img, (512,0),(100,512), (0,255,0), 3)
cv2.imshow("Line", img)
cv2.waitKey(0)

# dikdörtgen
# (resim, başlangıç, bitiş, renk, doldurma komutu)
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Rectengle", img)
cv2.waitKey(0)

# çember
# (resim, merkez noktası, yarıçapı, renk, doldurma komutu)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Circle", img)
cv2.waitKey(0)

# metin
cv2.putText(img, "Bir seyler yazsin",(0,250), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Yazı", img)
cv2.waitKey(0)