import cv2
import time

video_name = "v1.mp4"

cap = cv2.VideoCapture(video_name)

print("Genislik: ", cap.get(3))
print("Yukseklik: ", cap.get(4))

#Elimizde video olmasa dahi yükler ama ilerde hata yaşarız.
#Hata almamak için aşağıdaki kodu mutlaka yazmalıyız.

if cap.isOpened() == False:
    print("Hata")

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01) #Kullanmazsak çok hızlı akar

        cv2.imshow("Video", frame)
    else: break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()