import os
import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(script_dir, '..', 'audio', 'Ethereal Alien Dreamscape.wav')

sample_rate, amplitude = read(audio_path)

left_channel = amplitude[:, 0]
right_channel = amplitude[:, 1]

mean_left = np.mean(left_channel)
mean_right = np.mean(right_channel)

length = len(left_channel)/48000

plt.plot(left_channel)
# plt.plot(right_channel)
plt.show()
