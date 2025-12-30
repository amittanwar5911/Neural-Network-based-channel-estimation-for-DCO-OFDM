from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

def build_model(num_taps):
    model = Sequential([
        Dense(64, activation='relu', input_dim=2),
        Dense(64, activation='relu'),
        Dense(num_taps)
    ])
    model.compile(optimizer=Adam(0.001), loss='mse')
    return model
