import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#1. створюємо функцію для генерації фігур
def generate_image(color, shape):
    img = np.zeros((200, 200, 3), np.uint8)
    if shape == 'circle':
        cv2.circle(img, (100, 100), 50, color, -1)
    elif shape == 'square':
        cv2.rectangle(img, (50, 50), (150, 150), color, -1)
    elif shape == 'triangle':
        points = np.array([[100, 40], [40, 160], [160, 160]])
        cv2.drawContours(img, [points], 0, color, -1)

    return img

#2. формуємо набір даних
X = [] #список ознак
y = [] #cписок міток

colors = {
    'red' : (255, 0, 0),
    'green' : (0, 255, 0),
    'blue' : (0, 0, 255),
    'yellow' : (255, 255, 0)
}

shapes = ['circle', 'square', 'triangle']
for color_name in colors.items():
    for shape in shapes:
        for _ in range(10):
            img = generate_image(color_name, shape)
            mean_color = cv2.mean(img)[:3] #B, G, R, alpha
