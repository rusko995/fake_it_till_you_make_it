# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:59:32 2020

@author: Asus
"""

import pyaudio
import wave

NOW_PLAYING = False
CHUNK = 1024

class Play_voice():

    global CHUNK
    
    def __init__(self):   
        # instantiate PyAudio (1)
        self.p = pyaudio.PyAudio()
        self.wf = wave.open('output.wav', 'rb')
        # open stream (2)
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True)
        
        # read data
        self.data = self.wf.readframes(CHUNK)
        #
    
    def play_sound(self):
        global NOW_PLAYING
        NOW_PLAYING = True
    ## play stream (3)
        while len(self.data) > 0 and NOW_PLAYING:
            self.stream.write(self.data)
            self.data = self.wf.readframes(CHUNK)
            
    def pause_sound(self):
        # stop stream (4)
        global NOW_PLAYING
        self.stream.stop_stream()
        NOW_PLAYING = False
        
    def stop_sound(self):
        global NOW_PLAYING
        self.stream.close()
    
        # close PyAudio (5)
        self.p.terminate()
        NOW_PLAYING = False
        
  