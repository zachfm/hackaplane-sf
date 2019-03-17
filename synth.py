import numpy
import math

def triangle(f, length, rate):
    n = int(length * rate)
    t = numpy.arange(n) / rate
    x = linspace(0,0,n)
    harmonics = [1, 3, 5, 7, 9, 11, 13]
    for h in harmonics:
        if h % 2 == 0:
            x += sin(2*pi*h*f*t)/(h**2)
        else:
            x -= sin(2*pi*h*f*t)/(h**2)
    return x