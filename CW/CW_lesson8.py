import cv2
import numpy as np

# face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface_improved.xml')
# eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_smile.xml')
face_net = cv2.dnn.readNetFromCaffe('data/DNN/deploy.prototxt', 'data/DNN/res10_300x300_ssd_iter_140000.caffemodel')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize = (30, 30)) #scaleFactor - коефіцієнт зменшення зображення або іншими словами масштабування,
    # # minNeighbors - кількість перевірок, шоб провірити обличчя, minSize - мінімальне вікно обличчя
    # # print(faces)
    # for (x,y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
    #
    #     roi_gray = gray[y:y+h, x:x+w] #зріз тої частини зображення, де знаходиться обличчя, вона тільки нам важлива, все інше відсікаємо
    #     roi_color = frame[y:y+h, x:x+w]
    #
    #     eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10, minSize = (15, 15))
    #     for (ex,ey,ew,eh) in eyes:
    #         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 1)
    #
    #     smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 10, minSize = (25, 25))
    #     for (sx,sy,sw,sh) in smiles:
    #         cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 255), 1)
    #
    # cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)



    if not ret:
        break

    (h, w) = frame.shape[:2] #метод shape показує нам висоту,
    # довжину і кількість кольорових потоків. Тут ми зазначеємо, що нам треба лише перші дві змінні висота і довжина

    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0)) #
    face_net.setInput(blob) #передає наше зображення в нейронну мережу
    detection = face_net.forward() #отримуємо назад результат
    for i in range(detection.shape[2]):



    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
