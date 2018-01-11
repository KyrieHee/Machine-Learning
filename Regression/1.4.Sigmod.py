#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(b=True, ls='dotted')
plt.title('Sigmod function', fontsize=18)
plt.plot(x,sig)
plt.show()