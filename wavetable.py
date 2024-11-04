import numpy as np
import scipy.io.wavfile as wav

def interpolate_linearly(wave_table, index):
    # Calculate the indices for linear interpolation
    truncated_index = int(np.floor(index))
    next_index = (truncated_index + 1) % wave_table.shape[0]

    # Corrected assignment operator
    next_index_weight = index - truncated_index
    truncated_index_weight = 1 - next_index_weight
    
    # Perform linear interpolation
    return (truncated_index_weight * wave_table[truncated_index] +
            next_index_weight * wave_table[next_index])

def main():
    sample_rate = 44100
    f = 440  # Frequency in Hz (440 Hz for an A note)
    t = 3    # Duration in seconds

    wavetable_length = 32
    wave_table = np.zeros((wavetable_length,))

    # Create the wavetable
    for n in range(wavetable_length):
        wave_table[n] = np.sin(2 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate))

    index = 0
    index_increment = f * wavetable_length / sample_rate

    # Generate the output signal
    for n in range(output.shape[0]):
        output[n] = interpolate_linearly(wave_table, index)
        index += index_increment
        index %= wavetable_length 

    gain = -20  # Test with -20 dB gain
    amplitude = 10 ** (gain / 20)
    output *= amplitude

    # Normalize the output to prevent clipping
    output = np.clip(output, -1.0, 1.0)

    wav.write("Sine440hz.wav", sample_rate, output.astype(np.float32))

if __name__ == '__main__':
    main()
