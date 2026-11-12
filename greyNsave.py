
import cv2

# Read the original image
img = cv2.imread("photo.jpg")

# Check if image loaded successfully
if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display grayscale image
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    cv2.imwrite("grayscale.jpg", gray)

    print("Image saved successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
