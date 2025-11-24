import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.python.layers.normalization import normalization

train_ds = tf.keras.preprocessing.image_dataset_from_directory('data/dataset/train_set',
            image_size=(128, 128), batch_size=32,
            label_mode='categorical')
test_ds = tf.keras.preprocessing.image_dataset_from_directory('data/dataset/test_set',
            image_size=(128, 128), batch_size=32,
            label_mode='categorical')

#3. НОРМАЛІЗАЦІЯ ЗОБРАЖЕНЬ
normalization_layer = layers.Rescaling(1./255)
train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y))

#4. ВХІДНИЙ ШАР
model = models.Sequential()

model.add(layers.Conv2D(filters = 32, kernel_size = (3, 3),
                        activation = 'relu', input_shape = (128, 128, 3)))

model.add(layers.MaxPooling2D(2, 2))

model.add(layers.Conv2D(filters = 62, kernel_size = (3, 3),
                        activation = 'relu'))
model.add(layers.MaxPooling2D(2, 2))

model.add(layers.Conv2D(filters = 128, kernel_size = (3, 3),
                        activation = 'relu'))
model.add(layers.MaxPooling2D(2, 2))

model.add(layers.Conv2D(256, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(2,2))

model.add(layers.Flatten())

#5.ШАР
model.add(layers.Dense(32, activation = 'relu'))
model.add(layers.Dense(3, activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.summary()
history = model.fit(train_ds,
                    validation_data=test_ds,
                    epochs=15,
                    verbose=2)
test_loss, test_acc = model.evaluate(test_ds)
print(f'Якість: {test_acc}')

#6. ПЕРЕВІРКА.
class_name = ['apple', 'banana', 'orange']
img = image.load_img('Images/oilk,9876-400x400.png', target_size = (128, 128))
img_array = image.img_to_array(img)
img_array = img_array / 255.0

img_array = np.expand_dims(img_array, axis = 0)
predictions = model.predict(img_array)

predicted_index = np.argmax(predictions[0])

print(f'Імовірність по класам: {predictions[0]}')

print(f'Модель визначила: {class_name[predicted_index]}')
