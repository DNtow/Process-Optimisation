import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample data preparation
X_train = np.array([[1], [2], [3], [4]], dtype=float)
y_train = np.array([[1], [4], [9], [16]], dtype=float)  # Example target values

X_test = np.array([[5], [6], [7], [8]], dtype=float)
y_test = np.array([[25], [36], [49], [64]], dtype=float)  # Example target values

# Define and fit the scaler
scaler_y = MinMaxScaler()
scaler_y.fit(y_train)  # Fit scaler on the training data

# Scale the training and test target values
y_train_scaled = scaler_y.transform(y_train)
y_test_scaled = scaler_y.transform(y_test)

# Define and compile a simple model
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train_scaled, epochs=10, verbose=1)

# Make predictions
y_pred_scaled = model.predict(X_test)

# Inverse transform the predictions and test targets
y_pred_original = scaler_y.inverse_transform(y_pred_scaled)
y_test_original = scaler_y.inverse_transform(y_test_scaled)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(y_test_original, label='Actual Values', color='blue')
plt.plot(y_pred_original, label='Predicted Values', color='red', linestyle='dashed')
plt.xlabel('Sample Index')
plt.ylabel('Values')
plt.title('Actual vs Predicted Values')
plt.legend()
plt.show()