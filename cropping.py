import cv2

img = cv2.imread("photo.jpg")

if img is None:
    print("Image not found!")
else:
    # Crop image
    cropped = img[100:400, 150:450]

    # Display cropped image
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped Image", cropped)

    # Save cropped image
    cv2.imwrite("cropped.jpg", cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
