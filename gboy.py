#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division
import math
import numpy

import pyaudio # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

stream = None
file = []

def c_major_map(note, octave):
    base_freq = 0
    if note == 0:
        return 0
    #C
    if note == 1:
        base_freq = 16.35
    #C#
    if note == 1.5:
        base_freq = 17.32
    #D
    if note == 2:
        base_freq = 18.35
    #D#
    if note == 2.5:
        base_freq = 19.45
    #E
    if note == 3:
        base_freq = 20.60
    #F
    if note == 4:
        base_freq = 21.83
    #F#
    if note == 4.5:
        base_freq = 23.12
    #G
    if note == 5:
        base_freq = 24.50
    #G#
    if note == 5.5:
        base_freq = 25.96
    #A
    if note == 6:
        base_freq = 27.50
    #A#
    if note == 6.5:
        base_freq = 29.14
    #B
    if note == 7:
        base_freq = 30.87
    return base_freq * (2 ** octave)
        

def play_note(note, octave, duration, volume=0.1):
    duration = duration / 40
    octave = octave + 1
    play_tone(c_major_map(note, octave), duration, 44100)

def triangle_chord(f1, f2, length, rate):
    return triangle(f1, length, rate) + triangle(f2, length, rate)

def triangle(f, length, rate):
    n = int(length * rate)
    t = numpy.arange(n) / rate
    x = numpy.linspace(0,0,n)
    harmonics = [1, 3, 5, 7, 9, 11, 13]
    for h in harmonics:
        if h % 2 == 0:
            x += numpy.sin(2*3.14*h*f*t)/(h**2)
        else:
            x -= numpy.sin(2*3.14*h*f*t)/(h**2)
    return x

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(frequency=440, length=1, rate=44100):
    chunks = []
    chunks.append(triangle(frequency, length, rate)*numpy.concatenate([numpy.linspace(0,1,100), numpy.linspace(1,1,length*rate-200), numpy.linspace(1,0,100)]))

    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())

def play_chord(f1, f2, length=1, rate=44100):
    chunks = []
    chunks.append(triangle_chord(f1, f2, length, rate)*numpy.concatenate([numpy.linspace(0,1,100), numpy.linspace(1,1,length*rate-200), numpy.linspace(1,0,100)]))

    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())

def play_note_chord(note1, octave1, note2, octave2, duration, volume=0.1):
    duration = duration / 40
    octave1 = octave1 + 1
    octave2 = octave2 + 1
    play_chord(c_major_map(note1, octave1), c_major_map(note2, octave2), duration, 44100)


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)

    #cave story
    play_note_chord(1, 3, 5, 3, 12)
    play_note_chord(1, 4, 5, 3, 12)
    play_note_chord(1, 3, 5, 3, 12)
    play_note_chord(1, 4, 5, 3, 12)
    play_note_chord(1, 3, 4.5, 3, 12)
    play_note_chord(1, 4, 4.5, 3, 12)
    play_note_chord(1, 3, 4.5, 3, 12)
    play_note_chord(1, 4, 4.5, 3, 12)
    play_note_chord(1, 3, 4, 3, 12)
    play_note_chord(1, 4, 4, 3, 12)
    play_note_chord(1, 3, 4, 3, 12)
    play_note_chord(1, 4, 4, 3, 12)
    play_note_chord(1, 3, 3, 3, 12)
    play_note_chord(1, 4, 3.5, 3, 12)
    play_note(3, 3, 9)
    play_note(3, 3, 3)
    play_note(4, 3, 9)
    play_note(4.5, 3, 3)
    play_note(5, 3, 12)
    play_note(1, 4, 12)
    play_note(5, 3, 12)
    play_note(1, 4, 12)
    play_note(4.5, 3, 12)
    play_note(1, 4, 12)
    play_note(4.5, 3, 12)
    play_note(1, 4, 12)
    play_note(4, 3, 12)
    play_note(1, 4, 12)
    play_note(4, 3, 12)
    play_note(1, 4, 12)
    play_note(2.5, 4, 12)
    play_note(2, 4, 12)
    play_note(1, 4, 12)
    play_note(0, 4, 12)
    #chorus
    play_note(5, 3, 12)
    play_note(6, 3, 9)
    play_note(6, 3, 3)
    play_note(6.5, 3, 9)
    play_note(1, 4, 3)
    play_note(6.5, 3, 9)
    play_note(6, 3, 3)
    play_note(5, 3, 12)
    play_note(2, 3, 12)
    play_note(6.5, 3, 9)
    play_note(1, 4, 3)
    play_note(6.5, 3, 9)
    play_note(6, 3, 3)
    play_note(5, 3, 12)
    play_note(2.5, 3, 12)
    play_note(6.5, 3, 9)
    play_note(6.5, 3, 3)
    play_note(6, 3, 9)
    play_note(5, 3, 3)
    play_note(6, 3, 12)
    play_note(4, 3, 12)
    play_note(1, 4, 9)
    play_note(1, 4, 3)
    play_note(6, 3, 12)


    #william tell overture
    play_note(0, 0, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(0, 0, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(0, 0, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(1, 3, 12, 0.1)
    play_note(2, 3, 12, 0.1)
    play_note(3, 3, 12, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(0, 0, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(1, 3, 6, 0.1)
    play_note(0, 0, 6, 0.1)
    play_note(3, 3, 6, 0.1)
    play_note(3, 3, 6, 0.1)
    play_note(2, 3, 12, 0.1)
    play_note(7, 2, 12, 0.1)
    play_note(5, 2, 12, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(0, 0, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(0, 0, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(5, 2, 6, 0.1)
    play_note(1, 3, 12, 0.1)
    play_note(2, 3, 12, 0.1)
    play_note(3, 3, 12, 0.1)
    play_note(1, 3, 6, 0.1)
    play_note(3, 3, 6, 0.1)
    play_note(5, 3, 30, 0.1)
    play_note(4, 3, 6, 0.1)
    play_note(3, 3, 6, 0.1)
    play_note(2, 3, 6, 0.1)
    play_note(1, 3, 12, 0.1)
    play_note(3, 3, 12, 0.1)
    play_note(1, 3, 12, 0.1)
    play_note(0, 0, 6, 0.1)

    #sea shanty
    play_note(1, 3, 5, 0.1)
    play_note(7, 2, 5, 0.1)
    play_note(1, 3, 11, 0.1)
    play_note(1, 2, 11, 0.1)
    play_note(1, 2, 11, 0.1)
    play_note(5, 2, 5, 0.1)
    play_note(4, 2, 5, 0.1)
    play_note(3, 2, 5, 0.1)
    play_note(5, 2, 5, 0.1)
    play_note(1, 3, 11, 0.1)
    play_note(1, 3, 11, 0.1)
    play_note(0, 0, 6, 0.1)

    #dragnet
    play_note(1, 2, 75, 0.1)
    play_note(2, 2, 15, 0.1)
    play_note(3, 2, 30, 0.1)
    play_note(1, 2, 60, 0.1)
    play_note(1, 2, 60, 0.1)
    play_note(1, 2, 75, 0.1)
    play_note(2, 2, 15, 0.1)
    play_note(3, 2, 30, 0.1)
    play_note(1, 2, 30, 0.1)
    play_note(1, 2, 7, 0.1)
    play_note(5, 2, 83, 0.1)
    play_note(1, 2, 30, 0.1)
    play_note(0, 0, 6, 0.1)


    stream.close()
    p.terminate()
