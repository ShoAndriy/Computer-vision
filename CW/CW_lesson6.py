from typing import ClassVar

import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (5, 5), 2)
gray1 = cv2.convertScaleAbs(gray1, alpha=2.5, beta=10)
cv2.imshow('Video1', gray1)
cv2.imshow('Video2', frame1)


while True: #показувати трансляцію
    ret, frame2 = cap.read()
    if not ret:
        print("Кадри скінчились")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (5, 5), 2)
    gray2 = cv2.convertScaleAbs(gray2, alpha=2.5, beta=10)
    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 700:
            perimeter = cv2.arcLength(cnt, True)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            M = cv2.moments(cnt)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
            cv2.circle(frame2, (cx, cy), 3, (0, 0, 255), -1)
    gray1 = gray2
    cv2.imshow('Video1', gray2)
    cv2.imshow('Video2', frame2)



#КОНСПЕКТ
# cap = cv2.VideoCapture(0) # значення 0 - зчитувати дані з камери
# ret, frame = cap.read() # змінні ret i frame зчитують дані безкінечно (в циклі) за допомогою команди cap.read()
# 0xFF == ord('q') - код клавіши "q", використовується, щоб при нажиманні клавіши виконувалися певні задані дії


cap.release() #звільняє камеру від використання, тепер можна переключитися з PyCharm на Google Meet
cv2.destroyAllWindows()
