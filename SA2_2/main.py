# Importing Library
import numpy as np
import cv2


inputPath = 'static/lion.png'


originalImage = cv2.imread(inputPath)


# ------------Convert image to Grayscale --------------

grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale Image', grayscaleImage)
cv2.waitKey(0)


# ----------------- Convert image to Oil Painting -----------------------

# Apply the oil painting effect
oilImg = cv2.xphoto.oilPainting(originalImage, size=7, dynRatio=1)

# Display the converted image
cv2.imshow('Oil Paint Image', oilImg)
cv2.waitKey(0)
