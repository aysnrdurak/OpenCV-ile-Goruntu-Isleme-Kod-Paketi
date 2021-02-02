import cv2

#içe aktarma:
img = cv2.imread("p1.png",0)
# 0 resmi siyah beyaz olarak elde etmemizi sağlar.

#görselleştir
cv2.imshow("Resim", img)

#resmi bekletme komutumuz:
k = cv2.waitKey(0) &0xFF
if k == 27: #esc nin karşılığıdır.
    cv2.destroyAllWindows()
elif k == ord("s"): #s tuşuna basarsak...
    cv2.imwrite("p1_saved.png", img)
    cv2.destroyAllWindows()
