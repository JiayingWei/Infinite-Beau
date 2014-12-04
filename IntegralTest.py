# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 20:13:01 2014

@author: elena
"""

from scipy.integrate import quad
import math

def integrand(x):
    return math.cos(x)

pi = math.pi
(ans, err) = quad(integrand, 0, pi/2)
print type(ans)