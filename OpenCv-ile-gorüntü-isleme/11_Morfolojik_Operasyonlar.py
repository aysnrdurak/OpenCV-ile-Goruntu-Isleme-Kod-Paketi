import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("stars.png")
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal"), plt.show(block = False)

#erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 3)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon"), plt.show(block = False)

#genişleme dilation
result2 = cv2.dilate(img, kernel, iterations = 3)
plt.figure(), plt.imshow(result2, cmap = "gray" ), plt.axis("off"), plt.title("Genişleme"), plt.show(block = False)

# açılma için white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:3])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray" ), plt.axis("off"), plt.title("White Noise"), plt.show(block = False)
noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray" ), plt.axis("off"), plt.title("img with White Noise"), plt.show(block = False)

#açılma 
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray" ), plt.axis("off"), plt.title("Opening"), plt.show()

# black noise
blackNoise = np.random.randint(0,2, size = img.shape)
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise"), plt.show()

black_noise_img = blackNoise + img 
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Img"), plt.show()

# kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Kapama"), plt.show()

# gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan"), plt.show()
