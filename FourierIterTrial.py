# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 19:28:58 2014

@author: Elena
"""
from scipy.integrate import quad
import math

def function(x):
    return f(x)
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)

N = #define depth
pi = math.pi
period = 
w0 = 2*pi/period #T0 = 2L
#ans, err = quad(integrand, 0, pi/2)
#print ans
a0, err = (2/period)*quad(function, -1*period, period)
x_t = a0/2

def find_constants():
    for n in range(N):
        list_of_constants = []    
        def Aintegrand(x):    
            return function(x)*sin(n*w0*x)
        def Bintegrand(x):
            return function(x)*cos(n*w0*x)    
        
        an, err = (2/period)*quad(Aintegrand, -1*period, period)
        list_of_constant.append(an)
        bn, err = (2/period)*quad(Bintegrand, -1*period, period)     
        list_of_constants.append(bn)    
    return list_of_constants
   
def Sigma(n,t):    
    if n == 0:
        return x_t

    else:
        n = n-1
        sigma = list_of_constants[n*2]*sin(n*w0*t)+list_of_constants[n*2+1]*cos(n*w0*t)+ Sigma(n,t)
        return sigma
    
    
    
    
    
    
    