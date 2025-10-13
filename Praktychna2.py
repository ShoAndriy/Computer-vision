import cv2
import numpy as np

img = cv2.imread('Images/prakt.jpg')
scale = 2
img = cv2.resize(img, (int(img.shape[1] // scale), int(img.shape[0] // scale)))
img_copy = img.copy()
img = cv2.GaussianBlur(img, (9, 9), 2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


mask_red = cv2.inRange(img, (125, 100, 0), (179, 255, 255))
mask_blue = cv2.inRange(img, (54, 100, 0), (167, 255, 255))
mask_green = cv2.inRange(img, (40, 100, 0), (100, 255, 255))
mask_yellow = cv2.inRange(img, (8, 100, 0), (33, 255, 255))

mask_total = cv2.bitwise_or(mask_red, mask_blue)
mask_total = cv2.bitwise_or(mask_total, mask_green)
mask_total = cv2.bitwise_and(mask_total, mask_yellow)

lower = np.array([0, 100, 0])
upper = np.array([179, 255, 255])

mask_total = cv2.inRange(img, lower, upper)
img = cv2.bitwise_and(img, img, mask=mask_total)

contours, _ = cv2.findContours(mask_total, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt_red in contours_red:
        area = cv2.contourArea(cnt_red)
        if area > 200:
            x_red, y_red, w, h = cv2.boundingRect(cnt_red)
            y_red = int(y_red)
            x_red = int(x_red)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt_blue in contours_blue:
        area = cv2.contourArea(cnt_blue)
        if area > 200:
            x_blue, y_blue, w, h = cv2.boundingRect(cnt_blue)
            y_blue = int(y_blue)
            x_blue = int(x_blue)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt_green in contours_green:
        area = cv2.contourArea(cnt_green)
        if area > 200:
            x_green, y_green, w, h = cv2.boundingRect(cnt_green)
            y_green = int(y_green)
            x_green = int(x_green)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt_yellow in contours_yellow:
        area = cv2.contourArea(cnt_yellow)
        if area > 200:
            x_yellow, y_yellow, w, h = cv2.boundingRect(cnt_yellow)
            y_yellow = int(y_yellow)
            x_yellow = int(x_yellow)
    area = cv2.contourArea(cnt)
    if area > 200:
        x, y, w, h = cv2.boundingRect(cnt)
        if y == y_red and x == x_red:
            colour = 'red'
        elif y == y_blue and x == x_blue:
            colour = 'blue'
        elif y == y_green and x == x_green:
            colour = 'green'
        elif y == y_yellow and x == x_yellow:
            colour = 'yellow'
        else:
            colour = 'unknown'
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
        if len(approx) == 4:
            shape = "square"
        elif len(approx) == 3:
            shape = "triangle"
        elif len(approx) > 6:
            shape = "circle"
        else:
            shape = "other"

        cv2.putText(img_copy, f'S: {int(area)}, Sh: {shape}', (x - 5, y - 5 if y - 5 > 10 else y + 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1)
        cv2.putText(img_copy, f'Cl: {colour}, x, y:{x, y}', (x - 5, y - 25 if y - 25> 10 else y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 255), 1)
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(img_copy, (cx, cy), 3, (255, 0, 0), -1)



cv2.imshow('Image', img)
cv2.imshow('Mask', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.jpg', img_copy)