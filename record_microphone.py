# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:00:15 2020

@author: Asus
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:58:39 2020

@author: Asus
"""
from pynput import keyboard
import pyaudio
import wave
from random import choices
import time

NOW_RECORDING = False
frames = []


def make_it_worse(frames):
    """Makes the recording worse - as if your connection was bad."""
    n = len(frames)
    k = n//10
    samp = [1] + list(range(5,21)) #number of frames at next step
    probability = [0.84]+[0.01]*16 #probability of no. of frames
    r = 3 #how many times the frames repeate
    
    new_frames = []
    i = 0
    while i < n:
        k = choices(samp,probability)[0]
        if i+k < n:
            new_frames += frames[i:i+k]*r
            i = i+k
        else:
            new_frames += frames[i:]
            i=i+k
    return new_frames


class Record_voice():
    
    def __init__(self,output="new.wav"):
#        self.record = None
        self.output = output
#        print("self output is", self.output)
    
    
    def stop_recording(self):
        global NOW_RECORDING
        NOW_RECORDING = False
#        self.record = False
    
    def start_recording(self):
        global frames
        global NOW_RECORDING
        frames = []
        NOW_RECORDING = True
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        slow = 0.9 #if you put <1 the record plays slower
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        
        print("* recording")
        time.sleep(0.5)
        
        
        while NOW_RECORDING:
            data = stream.read(CHUNK)
            frames.append(data)
#            if not self.record:
#                break
#            time.sleep(0.01)
            
        
        print("* done recording") 
        
        new_frames = make_it_worse(frames)
        
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(self.output, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE*slow)
        wf.writeframes(b''.join(new_frames))
        wf.close()
        
        
        

class MyListener(keyboard.Listener):
    global frames
    def __init__(self,output='new.wav'):
        super(MyListener, self).__init__(self.on_press, self.on_release)
        self.key_pressed = None
        self.record = Record_voice(output)

    def on_press(self, key):
        if key == keyboard.Key.up:
            self.record.start_recording()
            

    def on_release(self, key):
        if key == keyboard.Key.up:
            self.record.stop_recording()
            
       
    def callback(self,in_data, frame_count, time_info, status):
        print("callback")
        if self.key_pressed == True:
            #stream_queue.put(in_data)
            print("record")
            frames.append(in_data)
            return (in_data, pyaudio.paContinue)
    
        elif self.key_pressed == False:
            #stream_queue.put(in_data)
            frames.append(in_data)
            return (in_data, pyaudio.paComplete)
    
        else:
            print("not record")
            return (in_data,pyaudio.paContinue)
  
if  __name__ == "__main__":    
    listener = MyListener('new.wav' )
    listener.start()
            