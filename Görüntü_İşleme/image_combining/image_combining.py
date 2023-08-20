
import cv2
import numpy as np

cat = cv2.imread('cat.jpg')
dog = cv2.imread('dog.jpg')

cat_2 = cv2.resize(cat, (400, 400))
dog_2 = cv2.resize(dog, (400, 400))

""" 1 - horizontal : yatay  """

horizontal = np.hstack((cat_2, dog_2))

""" 2 - vertical : dikey """

vertical = np.vstack((cat_2, dog_2))

cv2.imshow('image', horizontal)
cv2.imshow('image_2', vertical)

cv2.waitKey()
