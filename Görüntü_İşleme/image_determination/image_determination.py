
import cv2

image = cv2.imread('boat.jpg', 0)

_, threshold_Image = cv2.threshold(image, 80, 250, cv2.THRESH_BINARY)
threshold_Image_two = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 6)

cv2.imshow('image', image)
cv2.imshow('image_2', threshold_Image)
cv2.imshow('image_3', threshold_Image_two)

cv2.waitKey()
