import numpy as np
import cv2

image = cv2.imread("scale.jpg")
canvas = np.zeros_like(image, dtype="uint8")

red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)

cv2.line(canvas, (0,0), (300,300), green)
cv2.line(canvas, (300,0), (0, 300), red, 6) # 5th argument = 두께

cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.rectangle(canvas, (550,200), (200,225), red, 2)
cv2.rectangle(canvas, (200,50), (225,125), blue, -1) # 5th argument = -1(채우기)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

