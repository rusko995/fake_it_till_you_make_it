# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:58:39 2020

@author: Asus
"""

import pyaudio
import wave
from random import choices


def record_music():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    n = len(frames)
    k = n//10
    b0 = 4095*[0]
    samp = [1] + list(range(5, 21))
    probability = [0.84]+[0.01]*16

    new_frames = []
    i = 0
    while i < n:
        k = choices(samp, probability)[0]
        if i+k < n:
            new_frames += frames[i:i+k]*3
            i = i+k
        else:
            new_frames += frames[i:]
            i = i+k

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE*0.86)
    wf.writeframes(b''.join(new_frames))
    wf.close()
