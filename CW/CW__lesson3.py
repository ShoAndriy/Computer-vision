import cv2
import numpy as np

img = np.zeros((500,400, 3), np.uint8)
# img[:] = (199, 185, 116)
# rgb = bgr

# img[100:150, 200:250] = 199, 185, 116

cv2.rectangle(img, (100,100), (200,200), (199, 185, 116), 3)
cv2.line(img, (100,100), (200,200), (130, 185, 116), 3)
cv2.line(img, (0,img.shape[0] // 2),
         (img.shape[1],img.shape[0] // 2),
         (130, 120, 116), 3)
cv2.line(img, (img.shape[1] // 2, 0),
         (img.shape[1] // 2, img.shape[0]),
         (130, 120, 116), 3)
cv2.circle(img, (200, 200), 30, (0, 255, 255), 3)
cv2.putText(img, 'Komarov Ivan', (50, 80),
            cv2.FONT_HERSHEY_PLAIN, 3,
            (255, 0, 255), 3)


print(img.shape) #показує дані про вікно

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
