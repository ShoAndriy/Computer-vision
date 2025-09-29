# import cv2
# import numpy as np
import cv2

#IMAGES
# image = cv2.imread('Images/night-sky-9059825_1280.jpg')
# # image = cv2.resize(image, (600, 600))
# image = cv2.resize(image, (image.shape[1] // 2,
#                  image.shape[0] // 2))
# # image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# # image = cv2.flip(image, 0)
# # image = cv2.GaussianBlur(image, (19, 19), 0)
# # рівень розблюреності - тільки НЕПАРНІ числа
#
#
#
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# image = cv2.Canny(image, 100, 100)
#
# # image = cv2.dilate(image, None, iterations = 1) #робить обводку нашим контурам
# kernel = np.ones((5, 5), np.uint8)
# image = cv2.dilate(image, kernel, iterations = 1)
# image = cv2.erode(image, kernel, iterations = 1)
#
#
#
# cv2.imshow('space', image)
# # cv2.imshow('image', image[0:200, 0:400] )
# # print(image.shape)

#VIDEO

# video = cv2.VideoCapture("Videos/283431_small.mp4")
video = cv2.VideoCapture(0)
while True:
    mistake, frame = video.read() #метод читання зображення
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)
cv2.destroyAllWindows()