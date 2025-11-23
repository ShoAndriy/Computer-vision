import cv2
image = cv2.imread("Images/itsme.jpg")
image = cv2.resize(image, (500, 600))
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
image = cv2.Canny(image, 100, 100)

email = cv2.imread('Images/email.jpg')
email = cv2.resize(email, (500, 200))
email = cv2.cvtColor(email, cv2.COLOR_RGB2GRAY)
email = cv2.Canny(email, 400, 400)

email = cv2.imshow('Email', email)
image = cv2.imshow('Me', image)








cv2.waitKey(0)
cv2.destroyAllWindows()
