import cv2
import numpy as np

img = cv2.imread('Images/lol.jpg')
scale = 1
img = cv2.resize(img, (int(img.shape[1] // scale), int(img.shape[0] // scale)))

#make a copy
img_copy = img.copy()
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
img_copy_color = img.copy()

img_copy = cv2.GaussianBlur(img_copy, (5, 5), 2)
#розмиваємо фон, щоб полегшити комп'ютеру роботу

img_copy = cv2.equalizeHist(img_copy)
#посилення контрасту

img_copy = cv2.Canny(img_copy, 100, 150)
#задається певний діапазон, наскільки обширну кількість кольорів ти хочеш вивести

contours, hierarchy = cv2.findContours(img_copy,
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#пошук контурів
#RETR_EXTERNAL - РЕЖИМ ОТРИМАННЯ КОНТУРІВ, ЗНАХОДИТЬ КРАЙНІ КОНТУРИ
#кщо наш об'єкт має дірки, то вони будуть ігноруватися
#CHAIN_APPROX_SIMPLE - проксимація - процес наближення вираження
# одних величин або об'єктів через інші

#малювання контурів, прямокутників та тексту
#в циклі перебирається кожен контур
for cnt in contours:
    area = cv2.contourArea(cnt) #визначити площу контура
    if area > 50:
        x, y, w, h = cv2.boundingRect(cnt) #створює найменший прямокутник, який повністю містить в собі контур  #беремо 4 координати для 2 точок, щоб створити прямокутник
        cv2.drawContours(img_copy_color, [cnt], -1, (0, 255, 0), 2)
        cv2.rectangle(img_copy_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text_y = y - 5 if y - 5 > 10 else y + 15
        text = f'x: {x}, y: {y}, S: {int(area)}'
        cv2.putText(img_copy_color, text, (x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#[cnt] = список контурів, просто cnt - один контур, -1 - малювати всі контури  з масиву, колір, 2 - товщина



cv2.imshow('woman copy', img_copy)
cv2.imshow('woman', img)
cv2.imshow('woman copy color', img_copy_color)

cv2.waitKey(0)
cv2.destroyAllWindows()