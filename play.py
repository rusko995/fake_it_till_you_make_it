# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:28:09 2020

@author: Asus
"""

# import simpleaudio as sa
from playsound import playsound


def play_recording():
    # filename = 'output.wav'
    # wave_obj = sa.WaveObject.from_wave_file(filename)
    # play_obj = wave_obj.play()
    # play_obj.wait_done()  # Wait until sound has finished playing

    playsound('output.wav')
