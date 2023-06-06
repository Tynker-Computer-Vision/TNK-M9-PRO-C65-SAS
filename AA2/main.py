import numpy as np
import cv2

inputPath = 'static/img1.png'

# Load the color image
originalImage = cv2.imread(inputPath)


rotatedImage = cv2.rotate(originalImage, cv2.ROTATE_90_CLOCKWISE)

outputPath = 'converted/rotated.png'
cv2.imwrite(outputPath, rotatedImage)

cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)

print('Rotated image saved to disk : ' + outputPath)

# ------------Adjust contrast of the image --------------

# Change contrast of the image
contrastAdjustedImage = cv2.convertScaleAbs(rotatedImage, alpha=1.5, beta=-120)

# Save the image to disk
outputPath = 'converted/contrastAdjustedImage.png'
cv2.imwrite(outputPath, contrastAdjustedImage)

# Display the converted image
cv2.imshow('Contrast Adjusted Image', contrastAdjustedImage)
cv2.waitKey(0)


# Display a message indicating that the image has been saved
print('Contrast adjusted image saved to disk : ' + outputPath)
