# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 07:06:43 2020

@author: alex
"""

import tkinter as tk
from tkinter import ttk
import recorder

# --- functions ---

def combine_audio(vidname, audname, outname, fps=25):
    """merge video and audio file ....."""
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

def start():
    global running

    if running is not None:
        print('already running')
    else:
        running = rec.open('nonblocking.wav', 'wb')
        running.start_recording()

def stop():
    global running

    if running is not None:
        running.stop_recording()
        running.close()
        running = None
    else:
        print('not running')

# --- main ---

rec = recorder.Recorder(channels=2)
running = None

root = tk.Tk()
root.geometry('200x100')
root.title("Audio Rec..")
s = ttk.Style(root)
s.theme_use('clam')

button_rec = ttk.Button(root, text='Start Recording', command=start)
button_rec.pack(pady=10)

button_stop = ttk.Button(root, text='Stop Recording', command=stop)
button_stop.pack(pady=10)

root.mainloop() 