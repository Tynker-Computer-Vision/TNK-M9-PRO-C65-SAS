# Importing Library
import numpy as np
import cv2

# Define the input and output paths
inputPath = 'static/img1.png'

# Load the color image
orignalImage = cv2.imread(inputPath)

# ------------Rotate the image --------------

# Rotate the image
rotatedImage = cv2.rotate(orignalImage, cv2.ROTATE_90_CLOCKWISE)

# Save the image to disk
outputPath = 'converted/rotated.png'
cv2.imwrite(outputPath, rotatedImage)

# Display the image
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)


# Display a message indicating that the image has been saved
print('Rotated image saved to disk : ' + outputPath)
