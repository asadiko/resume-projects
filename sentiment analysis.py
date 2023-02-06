import tensorflow as tf
import numpy as np
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the data into a pandas dataframe
df = pd.read_csv('sentiment_data.csv')

# Pre-processing the data


def preprocess_text(text):
    text = text.lower()  # convert to lowercase
    # remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    text = text.split()  # split the text into words
    return text


df['text'] = df['text'].apply(preprocess_text)

# Tokenizing the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['text'].values)
word_index = tokenizer.word_index

# Encoding the text data
text_data = tokenizer.texts_to_sequences(df['text'].values)
text_data = pad_sequences(text_data)

# Split the data into train and test sets
train_data, test_data, train_labels, test_labels = train_test_split(
    text_data, df['sentiment'].values, test_size=0.2)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(
        word_index) + 1, output_dim=32, input_length=text_data.shape[1]),
    tf.keras.layers.LSTM(32, return_sequences=True),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(train_data, train_labels, epochs=10,
                    validation_data=(test_data, test_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_data, test_labels)
print("Test Loss: ", test_loss)
print("Test Accuracy: ", test_acc)
