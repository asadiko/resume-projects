#This code will build a speech recognition model using TensorFlow. 
# The speech data is loaded into a numpy array and preprocessed by converting the labels into one-hot encoded form. 
# The data is then split into training and test sets. 
# A simple convolutional neural network is created using the Keras API of TensorFlow and trained on the training data. 
# The performance of the model is visualized by plotting the accuracy and loss curves.
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv1D, MaxPool1D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

# Load the data into a numpy array
data = np.load('speech_data.npy')
labels = np.load('speech_labels.npy')

# Preprocess the data
num_classes = len(np.unique(labels))
labels = to_categorical(labels, num_classes)

# Split the data into train and test sets
train_data = data[:8000]
train_labels = labels[:8000]
test_data = data[8000:]
test_labels = labels[8000:]

# Create a model
model = tf.keras.Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(8000, 1)))
model.add(MaxPool1D(2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.01), metrics=['accuracy'])

# Train the model
history = model.fit(train_data, train_labels, epochs=10,
                    validation_data=(test_data, test_labels))

# Plot the accuracy and loss curves
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')

plt.figure()

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
