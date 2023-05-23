import cv2

image = cv2.imread("scale.jpg")

print(f"width : {image.shape[1]} pixels")
print(f"height : {image.shape[0]} pixels")
print(f"channels : {image.shape[2]} channels")

image = cv2.imread('scale.jpg')
corner = image[0:100, 0:200]
cv2.imshow("Corner", corner)

image[0:100, 0:200] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)