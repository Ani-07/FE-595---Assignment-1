# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

def sincosplot():
    time = np.arange(0,np.pi*2, 0.1) 
    sine_period = np.sin(time)
    cos_period = np.cos(time)
    plt.plot(time,sine_period)
    plt.plot(time,cos_period)
    plt.axhline(y=0)
    return plt.show()

sincosplot()

if __name__ == "__main__":
    sincosplot()
