
import cv2

sea = cv2.imread('sea.jpg')
space = cv2.imread('space.jpg')

sea_2 = cv2.resize(sea, (500, 500))
space_2 = cv2.resize(space, (500, 500))

combine = cv2.addWeighted(sea_2, 0.5, space_2, 0.5, 0)

cv2.imshow('image', combine)
cv2.waitKey()
