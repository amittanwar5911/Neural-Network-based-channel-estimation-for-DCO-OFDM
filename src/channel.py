import numpy as np

noise_var = 0.05

# Multipath real VLC channel
def apply_channel(x, h):
    y = np.convolve(x, h, mode='same')
    noise = np.random.normal(0, np.sqrt(noise_var), len(y))
    return y + noise
