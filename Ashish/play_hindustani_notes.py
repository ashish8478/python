import numpy as np
import sounddevice as my_sound_device
import math

f0_for_A_Note = 440  # A
tone_multiplier = 2.0 ** (1.0 / 12.0)

# tone_frequencies_for_12_notes = []
# for n in range(12):
#     tone_frequency_for_n = f0_for_A_Note * (tone_multiplier ** n)
#     tone_frequencies_for_12_notes.append(tone_frequency_for_n)
tone_frequencies_for_12_notes = [f0_for_A_Note * (tone_multiplier ** n) for n in range(12)]
audible_frequency = 44100
my_sound_device.default.samplerate = audible_frequency

note_play_time = 0.5 # half a second
speaker_volume = 1000  # 5000 works on Harshad Kaka's computer - change this.

# a list of numbers from 0, 1,2, 3,.... 44100/2
samples = [i / audible_frequency for i in range(int(audible_frequency * note_play_time))]

def get_tones_dict():
    western_tones = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    hindu_tones = ['S', 'r', 'R', 'g', 'G', 'm', 'M', 'P', 'd', 'D', 'n', 'N']
    western_tones_freqs = {}
    hindu_tones_freqs = {}

    for tone_index in range(len(western_tones)):
        western_tones_freqs[western_tones[tone_index]] = tone_frequencies_for_12_notes[tone_index]
        hindu_tones_freqs[hindu_tones[tone_index]] = tone_frequencies_for_12_notes[tone_index]

    return western_tones_freqs, hindu_tones_freqs


def get_note_freq(note_string):
    # note_string is two character string
    # e.g. "n-" which is komal Ni in lower octave
    # return this value: h_tones['n'] * 0.5
    multiplier = 1
    if note_string[1] == '-':
        multiplier = 0.5
    elif note_string[1] == '+':
        multiplier = 2
    else:
        multiplier = 1

    # return a number for the frequency
    tone_dict, htone_dict = get_tones_dict()
    freq = htone_dict[note_string[0]] * multiplier

    return freq


def play_notes(note_list):
    # start with an empty wave list
    wave = []
    notes = [note_list[i: i + 2] for i in range(0, len(note_list), 2)]
    # for each note in note_list find the frequency fr.
    for note in notes:
        fr = get_note_freq(note)
        # fr = htone_dict[note]
        # construct the note wave for that frequency like so:
        tone_wave = [np.int16(speaker_volume * np.sin(2 * np.pi * fr * samp_))
                     for samp_ in samples]
        # for frequency fr
        # and concatenate (+) the tone_wave for that frequency to "wave" list
        wave += tone_wave

    my_sound_device.play(wave, blocking=True)


# test_sample = 'srRgGmMPdDnNS'
# play_notes("S_r_G_m_P_D_n_S+")
# play_notes("S+n_D_P_m_G_r_S_")
# play_notes("S_R_G_S_R_m_P_D_m_P_N_S+")
# play_notes("S+P_D_m_G_S_R_G_S_N-S_")
# play_notes("P-N-S_R_G_S_R_P_m_G_R_S_N-S_")




'''
    converter = 1
    if note_string[1] == '-':
        converter = 0.5
    elif note_string[1] == '+':
        converter = 2
    else:
        converter = 1

    # return a number for the frequency
    tone_dict, htone_dict = get_tone_dict()
    freq = htone_dict[note_string[0]] * converter

    return freq

'''