#This code will perform time series forecasting using the ARIMA model from the statsmodels library. 
# The time series data is loaded into a pandas dataframe and plotted. 
# The data is then split into a training set and a test set. 
# The ARIMA model is fit to the training data and used to make predictions on the test data.
# The actual and predicted values are plotted, 
# and the mean squared error is calculated to evaluate the accuracy of the predictions.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Load the data into a pandas dataframe
df = pd.read_csv('time_series_data.csv', index_col='date', parse_dates=True)

# Plot the time series data
df.plot()
plt.show()

# Create a train and test split
train = df[:int(0.8*(len(df)))]
test = df[int(0.8*(len(df))):]

# Fit an ARIMA model
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()

# Make predictions
predictions = model_fit.forecast(steps=len(test))[0]

# Plot the actual vs predicted values
plt.plot(test.values)
plt.plot(predictions)
plt.show()

# Calculate the mean squared error
mse = mean_squared_error(test.values, predictions)
print("Mean Squared Error: ", mse)
