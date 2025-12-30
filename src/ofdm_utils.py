import numpy as np

# Parameters
N = 64
DC_bias = 3

# QPSK mapping
def qpsk_mod(bits):
    bits = bits.reshape((-1,2))
    mapping = {
        (0,0): 1+1j,
        (0,1): 1-1j,
        (1,0): -1+1j,
        (1,1): -1-1j
    }
    return np.array([mapping[tuple(b)] for b in bits]) / np.sqrt(2)

# Hermitian OFDM
def real_ofdm(symbols):
    X = np.zeros(N, dtype=complex)
    X[1:len(symbols)+1] = symbols
    X[-len(symbols):] = np.conj(symbols[::-1])
    x = np.fft.ifft(X) * np.sqrt(N)
    return np.real(x)

# DCO-OFDM
def dco_ofdm(x):
    x_bias = x + DC_bias
    return np.clip(x_bias, 0, None)
