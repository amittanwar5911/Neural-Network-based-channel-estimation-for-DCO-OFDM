import numpy as np
import matplotlib.pyplot as plt

from ofdm_utils import qpsk_mod, real_ofdm, dco_ofdm
from channel import apply_channel
from nn_model import build_model

# Parameters
N = 64
num_symbols = 2000
pilot_idx = np.arange(0, N//2, 4)

# True VLC channel
h_true = np.array([0.9, 0.35, 0.15])

# Training data
X_train = []
Y_train = []

for _ in range(num_symbols):
    bits = np.random.randint(0, 2, 2 * len(pilot_idx))
    qpsk = qpsk_mod(bits)
    x_ofdm = real_ofdm(qpsk)
    x_dco = dco_ofdm(x_ofdm)
    y = apply_channel(x_dco, h_true)

    for k in pilot_idx:
        X_train.append([x_dco[k], y[k]])
        Y_train.append(h_true)

X_train = np.array(X_train)
Y_train = np.array(Y_train)

# Build and train NN
model = build_model(len(h_true))
history = model.fit(X_train, Y_train, epochs=20, batch_size=128, verbose=0)

# Testing
bits = np.random.randint(0, 2, 2 * len(pilot_idx))
qpsk = qpsk_mod(bits)
x_ofdm = real_ofdm(qpsk)
x_dco = dco_ofdm(x_ofdm)
y = apply_channel(x_dco, h_true)

X_test = np.array([[x_dco[k], y[k]] for k in pilot_idx])
h_pred = model.predict(X_test)
h_est = np.mean(h_pred, axis=0)

print("TRUE h =", h_true)
print("ESTIMATED h =", h_est)

# Plots
plt.figure(figsize=(8,5))
plt.plot(history.history['loss'])
plt.title("Training MSE vs Epochs")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.grid()
plt.show()
