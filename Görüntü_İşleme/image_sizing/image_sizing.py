
import cv2
import time

image = cv2.imread('muhammed_ali.jpg', 0)
print('Fotograf boyutu :', image.shape)

cv2.imshow('firstImage', image)

#######################

""" sizing """

#######################

image2 = cv2.resize(image, (500, 500))
cv2.imshow('twoImage', image2)

######################

""" clipping """

######################

image3 = image[200:1000, 200:900]
cv2.imshow('treeImage', image3)

cv2.waitKey()
