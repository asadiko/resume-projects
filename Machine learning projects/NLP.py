import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Load the data into a list
texts = []
labels = [] # Add labels list
with open('nlp_data.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t') # Split line into text and label
        texts.append(line[0])
        labels.append(int(line[1])) # Convert label to int

# Tokenize the text data
tokenizer = Tokenizer(num_words=5000, oov_token='<OOV>')
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Pad the sequences to a common length
max_length = max([len(seq) for seq in sequences]) # Calculate maximum length of sequences
padded = pad_sequences(sequences, padding='post', maxlen=max_length) # Use max_length for padding

# Split the data into train and test sets
train_data = padded[:8000]
train_labels = labels[:8000]
test_data = padded[8000:]
test_labels = labels[8000:]

# Convert labels to numpy arrays
train_labels = np.array(train_labels)
test_labels = np.array(test_labels)

# Build a model
model = tf.keras.Sequential()
model.add(Embedding(input_dim=5000, output_dim=64,
          input_length=max_length)) # Use max_length for input length
model.add(LSTM(64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32))
model.add(Dropout(0.2))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(train_data, train_labels, epochs=10,
                    validation_data=(test_data, test_labels))
