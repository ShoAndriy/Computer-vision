import cv2
import numpy as np
from numpy.f2py.symbolic import as_real

img = cv2.imread('Images/selfie.png')
scale = 1.5
img = cv2.resize(img, (int(img.shape[1] // scale), int(img.shape[0] // scale)))

img_copy = img.copy()
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
img_copy_color = img.copy()


img_copy = cv2.Canny(img, 500, 100)
img_copy = cv2.GaussianBlur(img_copy, (7,7), 2)
img_copy = cv2.equalizeHist(img_copy)

counters, hierarchy = cv2.findContours(img_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in counters:
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.drawContours(img_copy_color, [cnt], -1, (0, 255, 0), 1)
        cv2.rectangle(img_copy_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text_y = y - 5 if y - 5 > 10 else y + 15
        text = f'x: {x}, y: {y}, S: {int(area)}'
        cv2.putText(img_copy_color, text, (x, text_y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

cv2.imshow('Myroslava and Andriy', img)
cv2.imshow('Myroslava and Andriy copy', img_copy)
cv2.imshow('Myroslava and Andriy copy color', img_copy_color)

cv2.waitKey(0)
cv2.destroyAllWindows()

