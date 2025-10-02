import cv2
import numpy as np

img = np.zeros((400,600, 3), np.uint8)
img[:] = (199, 185, 116)

me = cv2.imread('Images/myphoto.png')
me = cv2.resize(me, (160, 180))
img[20:20 + me.shape[0], 20:20 + me.shape[1]] = me

cv2.putText(img, 'Shobotenko Andriy', (200, 60),
            cv2.FONT_HERSHEY_PLAIN, 2,
            (0, 0, 0), 2)
cv2.putText(img, 'Computer Vision Student', (200, 90),
            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
            (0, 30, 0), 1)
cv2.putText(img, 'Email: andriyshobotenko@gmail.com', (200, 130),
            cv2.FONT_HERSHEY_PLAIN, 1.2,
            (0, 10, 0), 2)
cv2.putText(img, 'Phone: +380686911934', (200, 160),
            cv2.FONT_HERSHEY_PLAIN, 1.4,
            (0, 10, 0), 2)
cv2.putText(img, '14.10.2009', (200, 190),
            cv2.FONT_HERSHEY_PLAIN, 1.4,
            (0, 10, 0), 2)

qr = cv2.imread('Images/qrcode.png')
qr = cv2.resize(qr, (120, 120))
img[200:200 + qr.shape[0], 460:460 + qr.shape[1]] = qr

cv2.putText(img, 'OpenCV Business Card', (110, 370),
            cv2.FONT_HERSHEY_PLAIN, 2,
            (0, 10, 0), 2)

cv2.rectangle(img, (10,10), (590,390), (196, 76, 0), 3)


cv2.imshow('business_card', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("business_card.png", img)