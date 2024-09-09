# deep_learning_predictive_model.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

class DeepLearningPredictiveModel:
    def __init__(self, input_shape):
        self.model = Sequential([
            LSTM(64, activation='relu', input_shape=input_shape, return_sequences=True),
            LSTM(32, activation='relu'),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, X_train, y_train, epochs=20, batch_size=64):
        early_stopping = EarlyStopping(monitor='val_loss', patience=3)
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, callbacks=[early_stopping])

    def predict(self, X_test):
        return self.model.predict(X_test)

    def save_model(self, filename):
        self.model.save(filename)

    def load_model(self, filename):
        self.model = tf.keras.models.load_model(filename)
