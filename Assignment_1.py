import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from scipy.io import wavfile

file_path = "Assignment_1/vega.wav"

output_path = "output/output_"


def show_graph_bar(quantization_levels, snr_values):
    # Plotting the results as a bar graph
    plt.bar(quantization_levels, snr_values)
    plt.xlabel('Quantization Levels')
    plt.ylabel('SNR (dB)')
    plt.title('SNR vs. Quantization Levels')
    plt.grid(True)
    plt.show()

    pass


def show_graph_line(quantization_levels, snr_values):
    # Plotting the results as a line graph
    plt.plot(quantization_levels, snr_values, marker='o')
    plt.xlabel('Quantization Levels')
    plt.ylabel('SNR (dB)')
    plt.title('SNR vs. Quantization Levels')
    plt.grid(True)

    # Set x-axis ticks to quantization levels
    plt.xticks(quantization_levels)

    # Set fewer y-axis ticks for better readability
    num_ticks = min(len(snr_values), 5)  # Set a maximum of 5 y-axis ticks
    y_tick_step = (max(snr_values) - min(snr_values)) / (num_ticks - 1)
    plt.yticks(np.arange(min(snr_values), max(snr_values) + 1, y_tick_step))

    # Adjust tick parameters for better readability
    plt.tick_params(axis='x', which='both', direction='inout', labelsize=8)
    plt.tick_params(axis='y', which='both', direction='inout', labelsize=8)

    # Ensure labels fit in the plot area
    plt.tight_layout()

    plt.show()

def print_info(audio_signal,sample_rate,bits_per_sample):
    print("Audio Signal Shape:", audio_signal.shape)
    print("Sample Rate:", sample_rate)
    print("Bits Per Sample:", bits_per_sample)
    pass

def readwav(file_path):
    audio_signal, sample_rate = librosa.load(file_path, sr=None, mono=True)
    bits_per_sample = audio_signal.dtype.itemsize * 8

    return audio_signal, sample_rate, bits_per_sample


def quantizer(audio_signal,n):

    xq = np.floor((audio_signal + 1) * 2 ** (n - 1))
    xq = xq / (2 ** (n - 1))
    xq = xq - (2 ** n - 1) / (2 ** n)

    xe = audio_signal - xq
    return xe

# def compute_snr(signal, noise):
#     signal_power = np.sum(np.square(signal))
#     noise_power = np.sum(np.square(noise))
#     snr = 10 * np.log10(signal_power / noise_power)
#     return snr

def compute_snr(signal, noise):
    signal_var = np.var(signal)
    noise_var = np.var(noise)
    snr = 10 * np.log10(signal_var / noise_var)
    return snr
def Assignment_1():
    print(file_path)
    audio_signal, sample_rate, bits_per_sample = readwav(file_path)
    print_info(audio_signal, sample_rate, bits_per_sample)

    quantization_levels = np.arange(1, 16)
    snr_values = []

    for levels in quantization_levels:
        # output_audio_path = output_path + str(levels) + ".wav"
        quantized_signal = quantizer(audio_signal, levels)
        snr = compute_snr(audio_signal, quantized_signal)
        # wavfile.write(output_audio_path, sample_rate, quantized_signal)
        snr_values.append(snr)


    show_graph_line(quantization_levels,snr_values)
