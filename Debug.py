import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

print("Importing libraries...")

# Dummy data
x_train = np.array([[1], [2], [3], [4]], dtype=float)
y_train = np.array([[1], [4], [9], [16]], dtype=float)

# Define the model
model = Sequential([
    Dense(10, activation='relu', input_shape=[1]),
    Dense(1)
])

print("Model defined.")

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

print("Model compiled.")

# Train the model
history = model.fit(x_train, y_train, epochs=10, verbose=1)

print("Model training complete.")

# Evaluate the model
test_loss = model.evaluate(x_train, y_train, verbose=1)
print(f"Test Loss: {test_loss}")

# Make predictions
predictions = model.predict(x_train)
print(f"Predictions: {predictions}")