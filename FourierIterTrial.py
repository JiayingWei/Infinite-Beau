# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 19:28:58 2014

@author: Elena
"""
from scipy.integrate import quad
import math

def function(x):
    return 2*x
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)

pi = math.pi
period = pi
w0 = 2*pi/period #fundamental frequency
(a0, err) =quad(function, 0, period) #a0 is the series constant
x_t = (2/period)*a0/2

def find_constants(N):
    list_of_constants = [] 
    for n in range(N):   
        def Aintegrand(x):    
            return function(x)*sin(n*w0*x)
        def Bintegrand(x):
            return function(x)*cos(n*w0*x)    
        
        an, err = quad(Aintegrand, 0, period)
        an = (2/period)*an
        list_of_constants.append(an)
        bn, err = quad(Bintegrand, 0, period) 
        bn = (2/period)*bn
        list_of_constants.append(bn)  
    return list_of_constants
   
def Sigma(n,t):    
    constants = find_constants(3)    
    if n == 0:
        return x_t

    else:
        n = n-1
        sigma = constants[n]*sin(n*w0*t)+constants[n+1]*cos(n*w0*t)+ Sigma(n,t)
        return sigma
    
print Sigma(3,1)      