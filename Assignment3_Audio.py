import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram
import librosa
import librosa.display
from scipy.io import wavfile

output_path = "output/output_"

last_digit_audio_path = "Assignment_3/Recording.wav"
dtmf_audio_path = output_path + "dtmf_audio" + ".wav"
combined_audio_path = output_path + "combined_audio" + ".wav"

def readwav(file_path):
    audio_signal, sample_rate = librosa.load(file_path, sr=None, mono=True)
    bits_per_sample = audio_signal.dtype.itemsize * 8

    return audio_signal, sample_rate, bits_per_sample

def print_info(audio_signal,sample_rate,bits_per_sample):
    print("Audio Signal Shape:", audio_signal.shape)
    print("Sample Rate:", sample_rate)
    print("Bits Per Sample:", bits_per_sample)
    pass

def generate_dtmf_signal(digit, duration, fs):
    dtmf_freqs = {
        '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
        '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
        '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
        '*': (941, 1209), '0': (941, 1336), '#': (941, 1477)
    }
    f1, f2 = dtmf_freqs[digit]
    t = np.linspace(0, duration, int(duration * fs), endpoint=False)
    signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    return signal





def Assignment3_Audio():
    print(last_digit_audio_path)
    audio_signal, sample_rate, bits_per_sample = readwav(last_digit_audio_path)
    print_info(audio_signal, sample_rate, bits_per_sample)


    # Parameters
    duration = 1.0
    fs = 44100

    dtmf_signal = generate_dtmf_signal('8', duration, fs)

    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, duration, len(dtmf_signal)), dtmf_signal)
    plt.title('DTMF Signal (Digit "8") - Time Domain')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    wavfile.write(dtmf_audio_path, sample_rate, dtmf_signal)


    voice_recording = audio_signal

    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, duration, len(voice_recording)), voice_recording)
    plt.title('Voice Recording of Digit "8" - Time Domain')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    if len(dtmf_signal) < len(voice_recording):
        dtmf_signal = np.pad(dtmf_signal, (0, len(voice_recording) - len(dtmf_signal)), 'constant')
    elif len(dtmf_signal) > len(voice_recording):
        dtmf_signal = dtmf_signal[:len(voice_recording)]

    combined_signal = voice_recording + dtmf_signal

    wavfile.write(combined_audio_path, sample_rate, dtmf_signal)


    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, duration, len(combined_signal)), combined_signal)
    plt.title('Combined Signal - Time Domain')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    frequencies, spectrum = plt.psd(combined_signal, Fs=fs)

    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, 10 * np.log10(spectrum))
    plt.title('Spectrum of Combined Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power/Frequency (dB/Hz)')
    plt.grid(True)
    plt.show()

    f, t, Sxx = spectrogram(combined_signal, fs)

    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))
    plt.title('Spectrogram of Combined Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Power/Frequency (dB/Hz)')
    plt.show()

    pass