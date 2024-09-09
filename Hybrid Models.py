# hybrid_model.py
from sklearn.ensemble import RandomForestRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class HybridModel:
    def __init__(self):
        self.rf_model = RandomForestRegressor()
        self.dl_model = Sequential([
            Dense(64, activation='relu', input_shape=(10,)),
            Dense(32, activation='relu'),
            Dense(1)
        ])
        self.dl_model.compile(optimizer='adam', loss='mse')

    def train_rf(self, X_train, y_train):
        self.rf_model.fit(X_train, y_train)

    def train_dl(self, X_train, y_train, epochs=10, batch_size=32):
        self.dl_model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict_rf(self, X_test):
        return self.rf_model.predict(X_test)

    def predict_dl(self, X_test):
        return self.dl_model.predict(X_test)
