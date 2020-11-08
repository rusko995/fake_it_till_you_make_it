# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:59:32 2020

@author: Asus
"""

import pyaudio
import wave

CHUNK = 1024


wf = wave.open('last.wav', 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)
#
## play stream (3)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)
#
## stop stream (4)
#stream.stop_stream()
#stream.close()
#
## close PyAudio (5)
#p.terminate()