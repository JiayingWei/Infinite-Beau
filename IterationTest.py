# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 21:58:51 2014

@author: elena
"""
import math
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)

x_t = 1
w0 = 1
list_of_constants = [1,1,1,1,1,1]

def Sigma(N,t):    
    if N == 0:
        return x_t

    else:
        N = N-1
        sigma = list_of_constants[N*2]*sin(N*w0*t)+list_of_constants[N*2+1]*cos(N*w0*t)+ Sigma(N,t)
        return sigma

print Sigma(3,2*math.pi)