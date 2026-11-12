
import cv2

# Read image
img = cv2.imread("shapes.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, threshold = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY_INV
)

# Find contours
contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Process each shape
for contour in contours:

    # Ignore very small objects
    area = cv2.contourArea(contour)

    if area < 100:
        continue

    # Calculate perimeter
    perimeter = cv2.arcLength(contour, True)

    # Approximate shape
    approx = cv2.approxPolyDP(
        contour, 0.02 * perimeter, True
    )

    # Get bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    # Identify shape
    corners = len(approx)

    if corners == 3:
        shape = "Triangle"

    elif corners == 4:
        ratio = w / float(h)

        if 0.95 <= ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"

    elif corners > 7:
        shape = "Circle"

    else:
        shape = "Polygon"

    # Draw contour
    cv2.drawContours(
        img, [contour], -1, (0, 255, 0), 2
    )

    # Draw bounding box
    cv2.rectangle(
        img, (x, y), (x+w, y+h), (255, 0, 0), 2
    )

    # Display measurements
    cv2.putText(
        img, shape,
        (x, y - 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6, (0, 0, 255), 2
    )

    cv2.putText(
        img, f"Area: {area:.0f}",
        (x, y - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0, 0, 255), 2
    )

    cv2.putText(
        img, f"W:{w} H:{h}",
        (x, y + h + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 0, 0), 2
    )

    # Print measurements
    print("----------------------")
    print("Shape:", shape)
    print("Area:", area)
    print("Perimeter:", perimeter)
    print("Width:", w)
    print("Height:", h)

# Display result
cv2.imshow("Shape Detection", img)

# Save result
cv2.imwrite("detected_shapes.jpg", img)

print("\nImage saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
