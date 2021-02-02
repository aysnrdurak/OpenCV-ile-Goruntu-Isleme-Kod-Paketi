import cv2
import matplotlib.pyplot as plt 

img1 = cv2.imread("img1.JPG")
# resmimizi BGR'den RGB'ye dönüştürmek için:
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")

plt.figure()
plt.imshow(img1)
plt.waitforbuttonpress(0)

plt.figure()
plt.imshow(img2)
plt.waitforbuttonpress()

# shape aynı olmalı
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (600,600))
img2 = cv2.resize(img2, (600,600))

#karistirma
blended = cv2.addWeighted(src1 = img1, alpha = 0.1, src2 = img2, beta = 0.5, gamma = 0)
plt.figure()
plt.imshow(blended)
plt.waitforbuttonpress()