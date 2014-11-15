"""
Fourier Series is calculate based on the following process:

Given some function,
   x(t) = x_0 + SUM_from_1_to_depth(an*sin(fundamental_frequency * depth * t) + 
          bn*cos(fundamental_frequency * depth * t))
where an and bn are coefficients calculated as the definite integral of the 
given function over the course of a period at each depth
"""

from scipy.integrate import quad
import math, numpy
import matplotlib.pyplot as plt

from math import sin as sin
from math import cos as cos
from math import pi as pi


class Wave(object):
    """ Creates a wave object
    """
    def __init__(self, frequency):
#         self.amplitude = amplitude
         self.frequency = frequency
         self.period = 1/frequency
         self.fund_freq = 2*pi/self.period #fundamental freqeuncy
#         self.phase = phase


class Signal(Wave):
    """Creates a signal comprised of many waves (so an approximate of a signal)
    """
    def __init__(self, depth, frequency):
        super(Signal,self).__init__(frequency)        
        self.depth = depth     # define depth of approximation
        self.coefficients = []     # list of wave objects
        self.Amp_i = []
        self.alpha_i = []
        self.x_0 = 0
    
    def build(self):
        """ Uses recursion to create a approximation of a n depth signal (
        probably has to return a list which has to be turned into an 
        equation in calculate)
        """ 
        def functionR(x):
            return -10*cos(x)
        # def functionL(x):
        #     return -10*sin(x)
        
        (u0, err) = quad(functionR, -1*self.period, self.period) #u0 is the series constant
        # (u0_, err_) = quad(functionL, 0, self.period)  
        # u0 = u0 + u0_         
        self.u_0 = u0/self.period           
        
        for i in range(self.depth):
            def Aintegrand(x):    
                return functionR(x)*cos(i*self.fund_freq*x)
            def alphaintegrand(x):    
                return functionR(x)*sin(i*self.fund_freq*x)
 
            
            (Ai, err) = quad(Aintegrand, -1*self.period, self.period)
            # (Ai_,err_) = quad(Aintegrand, 0, self.period)
            # Ai = (Ai+Ai_) / self.period
            Ai = Ai / self.period
            self.coefficients.append(Ai)
            # self.Amp_i.append(Ai)
            (alphai, err) = quad(alphaintegrand, -1*self.period, self.period)
            alphai = math.asin(alphai / self.period)
            self.coefficients.append(alphai)
            # self.alpha_i.append(alphai)

            # self.coefficients.append(self.Amp_i) 
            # self.coefficients.append(self.alpha_i)
        return self.coefficients           


    def calculate(self,t):
        """ Calculates the value of the signal at time = t 
        """
        u_0 = self.u_0
        self.n = self.depth 
         
        def Sigma(x): 
            """ Uses recursion to build a signal that is evaluated at every t
            """
            if self.n == 0:
                return u_0
        
            else:
                self.n = self.n-1
                sigma = self.coefficients[self.n*2]*sin(self.n*self.fund_freq*t)+self.coefficients[self.n*2+1]*cos(self.n*self.fund_freq*t)+ Sigma(t)
                return sigma
        return Sigma(t)

def main():
    """builds all of the initial signals
    """
    signal1 = Signal(4, 1/(pi))    #set signal to depth 4 and frequency 1/pi
    signal2 = Signal(3, (1/(7*pi)))

    signal1.build()       #Build the constants necessary for the signal
    signal2.build()

    """plots all of the original signal vs the new signal
    """

    x = []
    y_original = []
    y_fourier = []
    for t in numpy.arange(0, 10,.1):
        x.append(t)
        y_original.append(-10*cos(t))
        y_fourier.append(signal1.calculate(t))

    plt.plot(x, y_original)
    plt.plot(x, y_fourier)
    plt.show()

    """parametrically plots signal1 vs signal2
    """

    sig1_original = []
    sig2_original = []
    sig1_fourier = []
    sig2_fourier = []

    for t in numpy.arange(0,10,.1):
        sig1_original.append(signal1.functionR(t))
        sig2_original.append(signal2.functionR(t))
        sig1_fourier.append(signal1.calculate(t))
        sig2_fourier.append(signal2.calculate(t))

    plt.plot(sig1_original, sig2_original)
    plt.show()
    plt.plot(sig1_fourier, sig2_fourier)
    plt.show()

if __name__ == '__main__':
    main()
