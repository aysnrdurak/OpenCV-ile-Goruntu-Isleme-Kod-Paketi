import cv2

# siyah beyaz elde etmek için 0 yazıyoruz.
#img = cv2.imread("p2.jpg",0)
#print("Boyutu: ", img.shape)
#cv2.imshow("Forografimiz", img)
#cv2.waitKey(2)

# renkli elde etmek için
img = cv2.imread("p2.jpg",)
print("Boyutu: ", img.shape)
cv2.imshow("RGB_Forografimiz", img)
cv2.waitKey(1)

# yeniden boyutlandırma
img800 = cv2.resize(img, (800,800))
print("img800_boyut: ", img800.shape)
cv2.imshow("img800", img800)
cv2.waitKey(1)

# kırpma
img_kirpik = img[200:500, 300:700] # height, width
cv2.imshow("Kirpik", img_kirpik)
cv2.waitKey(0)

