# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:05:17 2020

@author: 70880
"""

import math
import numpy as np
def f(x,w):
    return np.dot(x,w)
y=f([1,0,1,1,0,1],[1,2,3,4,5,6])
b=1
z=y+b
def sigmoid(z):
    return 1/(1+math.exp(-z))
print(sigmoid(z))