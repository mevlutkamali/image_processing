
import cv2

image = cv2.imread('image.jpg', 1)
"""
image_2 =cv2.resize(image, (900, 1200))
"""

print("Fotoğraf boyutu :", image.shape)

##########
""" line : çizgi """
##########

cv2.line(image, (0, 300), (400, 600), (100, 160, 100), 5)

##########
""" rectangle : dikdörtgen """
##########
"""
cv2.rectangle(image, (350, 200), (900, 700), (150, 0, 100), 4)
"""

###########
""" to steam : buğulamak """
###########
"""
cv2.rectangle(image, (350, 200), (900, 700), (150, 0, 100), cv2.FILLED)
"""

##########
""" circle : çember """
##########

cv2.circle(image, (650, 400), 250, (0, 100, 150), 4)
""" 250 = çap """

#########
""" text """
#########

cv2.putText(image, 'artificial_intelligence', (450, 300), cv2.FONT_ITALIC, 1, (255, 255 ,255), 3)

cv2.imshow('Foto_kayit',image)
cv2.waitKey()

