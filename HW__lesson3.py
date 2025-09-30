import cv2
import numpy as np

img = cv2.imread('Images/itsme.jpg')
img = cv2.resize(img, (400, 500))

cv2.rectangle(img, (130,135), (270,320), (40, 239, 4), 2)
cv2.putText(img, 'Andriy Shobotenko', (80, 350),
            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
            (40, 143, 4), 1)















cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()