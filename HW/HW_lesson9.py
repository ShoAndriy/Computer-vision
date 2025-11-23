import cv2
import os
from collections import Counter

net = cv2.dnn.readNetFromCaffe('data/MobileNet/mobilenet_deploy.prototxt', 'data/MobileNet/mobilenet.caffemodel')

classes = []
with open('data/MobileNet/synset.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(' ', 1)      # ділимо тільки на 2 частини: id і назва
        name = parts[1] if len(parts) > 1 else parts[0]
        classes.append(name)

image_folder = 'Images/MobileNet/'
results = []
class_counter = Counter()

for file_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, file_name)
    if not os.path.isfile(image_path):
        continue
    image = cv2.imread(image_path)
    if image is None:
        print(f"Попередження: Файл {file_name} не вдалося завантажити!")
        continue

    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (224, 224)),
        1.0 / 127.5,
        (224, 224),
        (127.5, 127.5, 127.5)
    )
    net.setInput(blob)
    preds = net.forward()
    idx = preds[0].argmax()
    label = classes[idx] if idx < len(classes) else "unknown"
    conf = float(preds[0][idx]) * 100
    results.append([file_name, label, round(conf, 2)])
    class_counter[label] += 1

print(f"{'Назва файлу':<20}{'Клас':<20}{'Ймовірність (%)':<20}")
print(f"{'-' * 60}")
for row in results:
    print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20.2f}")
print(f"{'-' * 60}")
print(f"{'Клас':<20}{'Кількість':<10}")
print(f"{'-' * 60}")
for label, count in class_counter.items():
    print(f"{label:<20}{count:<10}")



