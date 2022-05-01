import sounddevice as sd
import numpy as np
import math

f0 = 440  # A
a = 2.0 ** (1.0 / 12.0)
tone_fr = [f0 * (a ** n) for n in range(12)]
audible_freq = 44100 #for hooman ears
sd.default.samplerate = audible_freq
time = 0.5
# a list of numbers from 0, 1,2, 3,.... 44100/2
samples = [i / audible_freq for i in range(int(audible_freq * time))] #sampling freqs of notes
volume = 2000  #5000 works on Harshad Kaka's computer - change this.


def get_tone_dict(): #returns the notes and pairs them with their frequencies in a dictionary for western and hindustani
    tones = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    h_tones = ['S', 'r', 'R', 'g', 'G', 'm', 'M', 'P', 'd', 'D', 'n', 'N']
    tone_dict = {}
    htone_dict = {}
    for i in range(len(tones)):
        tone_dict[tones[i]] = tone_fr[i]
        htone_dict[h_tones[i]] = tone_fr[i]
    return tone_dict, htone_dict

 
def get_freq(note_string): #returns frequency of note in octave
    tone_dict, htone_dict = get_tone_dict()

    note = note_string[0]
    octave = note_string[1]

    frequency = htone_dict[note]

    if octave == '-':
        frequency = frequency * 0.5
    elif octave == '+':
        frequency = frequency * 2

    return frequency 


def play_notes(note_list): #plays notes sequentially by taking two charaters at a time: the note and its octave
    # start with an empty wave list
    wave = []
    notes = [note_list[i:i+2] for i in range(0, len(note_list), 2)]
    # for each note in note_list find the frequency fr.
    for note in notes:
        fr = get_freq(note)
        # construct the note wave 
        # for that frequency like so:
        tone_wave = [np.int16(volume * np.sin(2 * np.pi * fr * samp_)) for samp_ in samples]
        # for frequency fr
        # and concatenate (+) the tone_wave for that frequency to "wave" list
        wave += tone_wave
    sd.play(wave, blocking=True)

  
# test_sample = 'srRgGmMPdDnNS'
# play_notes("S_r_G_m_P_D_n_S+")
# play_notes("S+n_D_P_m_G_r_S_")
# play_notes("S_r_G_m_G_m_r_n-D-n-r_S_")
