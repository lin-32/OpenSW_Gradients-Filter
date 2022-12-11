import matplotlib.pyplot as plt
import cv2
img = cv2.imread('lion.jpeg')

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1)
blur = cv2.GaussianBlur(img, (0,0), 3)
blur2 = cv2.medianBlur(img, 3)
edge = cv2.Canny(img, cv2.CV_8U, 200, 255)


plt.figure(figsize=(15, 8))

plt.subplot(2, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis("off")

plt.subplot(2, 4, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.axis("off")
       
plt.subplot(2, 4, 3)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.axis("off")

plt.subplot(2, 4, 4)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.axis("off")

plt.subplot(2, 4, 5)
plt.imshow(edge, cmap='gray')
plt.title('Edge')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6)
plt.imshow(blur, cmap='gray')
plt.title('GaussianBlur')
plt.axis("off")

plt.subplot(2,4,7)
plt.imshow(blur2, cmap='gray')
plt.title('medianBlur')
plt.axis("off")

plt.tight_layout()
plt.show()
