#1. ЗАВАНТАЖУЄМО БІБЛІОТЕКИ
import pandas as pd #робота з даними у форматі таблиць
import numpy as np #математичні операції
import tensorflow as tf #бібліотека для нейронок
from tensorflow import keras #keras - бібліотека для tensorflow
from tensorflow.keras import layers #створення шарів нейронної мережі
from sklearn.preprocessing import LabelEncoder #для кодування міток
import matplotlib.pyplot as plt #для візуалізації даних, побудова гарфіків


#2. РОБОТА З CSV ФАЙЛОМ
df = pd.read_csv("data/figures_5types_2.csv")
#print(df.head())

encoder = LabelEncoder()
df['label_enc'] = encoder.fit_transform(df['label'])
df['area_perimeter_ratio'] = df['area'] / df['perimeter']

#3. ОБИРАЄМО ЕЛЕМЕНТИ ДЛЯ НАВЧАННЯ
X = df[['area', 'perimeter', 'corners', 'area_perimeter_ratio']]
y = df['label_enc']



#4. СТВОРЮЄМО МОДЕЛЬКУ
num_classes = len(encoder.classes_)
model = keras.Sequential([layers.Dense(16, activation = 'relu', input_shape = (4,)),
                         layers.Dense(16, activation = 'relu'),
                         layers.Dense(num_classes, activation='softmax')]) #створюємо перший шар #8 - кількість нейронів #input_shape = (3,) - скільки параметрів подається на навчання

#5. НАВЧАННЯ епоха - повний прохід всіх даних через мережу
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(X, y, epochs = 500, verbose = 0)

#6. ВІЗУАЛІЗАЦІЯ НАВЧАННЯ
plt.plot(history.history['loss'], label = 'Loss') #loss - втрата
plt.plot(history.history['accuracy'], label = 'Accuracy') #accuracy - точність
plt.xlabel('Епоха')
plt.ylabel('Значення')
plt.title('Learning process')
plt.legend()
plt.show()

#7. ТЕСТУВАННЯ

area = 25
perimeter = 20
corners = 0
ratio = area / perimeter

test = np.array([[area, perimeter, corners, ratio]])

pred = model.predict(test)
print(f'Імовірність по кожному класу: {pred}')
print(f'Модель визначила: {encoder.inverse_transform([np.argmax(pred)])}')

