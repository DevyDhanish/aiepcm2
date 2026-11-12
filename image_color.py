
import cv2
import numpy as np

# Load image
img = cv2.imread("photo.jpg")

if img is None:
    print("Image not found!")
    exit()

# 1. Grayscale Filter
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Red Filter
red = img.copy()
red[:, :, 0] = 0
red[:, :, 1] = 0

# 3. Green Filter
green = img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

# 4. Blue Filter
blue = img.copy()
blue[:, :, 1] = 0
blue[:, :, 2] = 0

# 5. Sepia Filter
sepia_matrix = np.array([
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]
])

sepia = cv2.transform(img, sepia_matrix)
sepia = np.clip(sepia, 0, 255).astype(np.uint8)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Red Filter", red)
cv2.imshow("Green Filter", green)
cv2.imshow("Blue Filter", blue)
cv2.imshow("Sepia Filter", sepia)

# Save images
cv2.imwrite("grayscale.jpg", gray)
cv2.imwrite("red.jpg", red)
cv2.imwrite("green.jpg", green)
cv2.imwrite("blue.jpg", blue)
cv2.imwrite("sepia.jpg", sepia)

print("All filtered images saved!")

cv2.waitKey(0)
cv2.destroyAllWindows()
