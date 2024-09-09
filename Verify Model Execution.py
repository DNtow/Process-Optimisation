import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Generate synthetic data
x = np.array([[i] for i in range(1, 101)], dtype=float)
y = np.array([[i] for i in range(1, 101)], dtype=float)

# Normalize the data
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x_scaled = scaler_x.fit_transform(x)
y_scaled = scaler_y.fit_transform(y)

# Split data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_scaled, test_size=0.2, random_state=42)

# Define and compile the model
model = Sequential([
    Input(shape=(x_train.shape[1],)),  # Define input shape
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=50, validation_split=0.1)

# Evaluate the model
loss = model.evaluate(x_test, y_test)
print("Test Loss:", loss)

# Predict on test data
predictions = model.predict(x_test)
# Inverse transform predictions and test data for better interpretation
predictions = scaler_y.inverse_transform(predictions)
x_test = scaler_x.inverse_transform(x_test)
print("Test Predictions:", predictions)