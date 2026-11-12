
import cv2

img = cv2.imread("photo.jpg")

if img is None:
    print("Image not found!")
else:
    # Rotate 90 degrees clockwise
    rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotate 90 degrees anticlockwise
    rotated_180 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Rotate 180 degrees
    rotated_270 = cv2.rotate(img, cv2.ROTATE_180)

    cv2.imshow("Original", img)
    cv2.imshow("90 Clockwise", rotated_90)
    cv2.imshow("90 Anticlockwise", rotated_180)
    cv2.imshow("180 Degrees", rotated_270)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
