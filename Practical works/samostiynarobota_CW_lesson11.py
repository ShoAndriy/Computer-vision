
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


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

colors = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
    "yellow": (0, 255, 255),
    "orange": (0, 128, 255),
    "purple": (255, 0, 255),
    "pink": (180, 105, 255),
    "white": (255, 255, 255)
}
X = []
y = []
samples_per_color = 100
noise_range = 20

shapes = ['circle', 'square', 'triangle']

for color_name, bgr in colors.items():
    base_color_data = np.array([bgr] * samples_per_color, dtype=np.int32)
    noise = np.random.randint(-noise_range, noise_range + 1, size=(samples_per_color, 3), dtype=np.int32)
    noisy_colors = base_color_data + noise
    noisy_colors = np.clip(noisy_colors, 0, 255)
    X.extend(noisy_colors.tolist())
    y.extend([color_name] * samples_per_color)
    for shape in shapes:
        for _ in range(10):
            img = generate_image(bgr, shape)
            mean_color = cv2.mean(img)[:3]
            features = [mean_color[0], mean_color[1], mean_color[2]]
            X.append(features)
            y.append(f"{color_name}_{shape}")
X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify = y)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Точність моделі:", round(accuracy * 100, 2), "%")

# test_img = generate_image((0, 255, 0), 'circle')
# mean_color = cv2.mean(test_img)[:3]
# prediction = model.predict([mean_color])
# print("Передбачення:", prediction[0])


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    lower = np.array([0, 40, 0])
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(frame, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            corners = len(approx)
            aspect_ratio = round(w / h, 2)

    cv2.imshow('tracking face', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


# cv2.imshow("Test image", test_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()