
import cv2

# Read image
img = cv2.imread("photo.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# -----------------------------
# IMAGE FILTERING
# -----------------------------

# Gaussian Blur
gaussian = cv2.GaussianBlur(
    img, (5, 5), 0
)

# Median Blur
median = cv2.medianBlur(
    img, 5
)

# Bilateral Filter
bilateral = cv2.bilateralFilter(
    img, 9, 75, 75
)


# -----------------------------
# EDGE DETECTION
# -----------------------------

# Canny Edge Detection
edges = cv2.Canny(
    gray, 100, 200
)

# Sobel Edge Detection
sobel_x = cv2.Sobel(
    gray, cv2.CV_64F, 1, 0, ksize=3
)

sobel_y = cv2.Sobel(
    gray, cv2.CV_64F, 0, 1, ksize=3
)

# Convert Sobel results to displayable images
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)


# -----------------------------
# DISPLAY RESULTS
# -----------------------------

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

cv2.imshow("Canny Edges", edges)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)


# -----------------------------
# SAVE RESULTS
# -----------------------------

cv2.imwrite("gaussian.jpg", gaussian)
cv2.imwrite("median.jpg", median)
cv2.imwrite("bilateral.jpg", bilateral)
cv2.imwrite("canny.jpg", edges)
cv2.imwrite("sobel_x.jpg", sobel_x)
cv2.imwrite("sobel_y.jpg", sobel_y)

print("All images processed and saved!")

cv2.waitKey(0)
cv2.destroyAllWindows()
