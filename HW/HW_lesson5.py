import cv2
import numpy as np
img = cv2.imread('Images/figures.png')
scale = 2
img = cv2.resize(img, (int(img.shape[1] // scale), int(img.shape[0] // scale)))
img_copy = img.copy()
img = cv2.GaussianBlur(img, (7,7), 2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0, 40, 0])
upper = np.array([179, 255, 255])
mask = cv2.inRange(img, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text_y = y - 5 if y - 5 > 10 else y + 15
        perimeter = cv2.arcLength(cnt, True)
        text = f'x: {x}, y: {y}, S: {int(area)}, P: {int(perimeter)}'
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        aspect_ratio = round(w / h, 2)
        compactness = round((4 * np.pi * area) / (perimeter **2), 2)
        approx = cv2.approxPolyDP(cnt, 0.01 * perimeter, True)
        if len(approx) == 4:
            shape = 'Quadrangle'
        elif len(approx) == 3:
            shape = 'Triangle'
        elif len(approx) > 8:
            shape = 'Oval'
        elif len(approx) == 5:
            shape = 'Pentagon/Star'
        else:
            shape = 'Another figure'

        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.circle(img_copy, (cx, cy), 3, (0, 0, 255), -1)
        cv2.putText(img_copy, text, (x, text_y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1)
        cv2.putText(img_copy, f'AR: {aspect_ratio}, C: {compactness}, Sh: {shape}',
                    (x, y - 25 if y - 25 > 10 else y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1)



cv2.imshow('image copy', img_copy)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Images/result.jpg', img_copy)
