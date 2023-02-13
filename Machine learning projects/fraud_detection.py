#This code will build a fraud detection system using a random forest classifier from the scikit-learn library. 
# The fraud data is loaded into a pandas dataframe and split into training and test sets. 
# A random forest classifier is trained on the training data and used to make predictions on the test data. 
# The performance of the model is evaluated using confusion matrix, precision, recall, and f1 score metrics.
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Load the data into a pandas dataframe
df = pd.read_csv('fraud_data.csv')

# Split the data into train and test sets
train_data, test_data, train_labels, test_labels = train_test_split(
    df.drop('fraud', axis=1), df['fraud'], test_size=0.2)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(train_data, train_labels)

# Make predictions on the test data
predictions = clf.predict(test_data)

# Evaluate the model
cm = confusion_matrix(test_labels, predictions)
precision = precision_score(test_labels, predictions)
recall = recall_score(test_labels, predictions)
f1 = f1_score(test_labels, predictions)

print("Confusion Matrix: \n", cm)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 Score: ", f1)
