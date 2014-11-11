"""
Fourier Series is calculate based on the following process:

Given some function,
   x(t) = x_0 + SUM_from_1_to_depth(an*sin(fundamental_frequency * depth * t) + 
          bn*cos(fundamental_frequency * depth * t))
where an and bn are coefficients calculated as the definite integral of the 
given function over the course of a period at each depth
"""

from scipy.integrate import quad
import math, pygame, numpy

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
        self.waves = []     # list of wave objects
        self.x_0 = 0
    
    def build(self):
        """ Uses recursion to create a approximation of a n depth signal (
        probably has to return a list which has to be turned into an 
        equation in calculate)
        """ 
        def functionR(x):
            return -10*cos(x)
        def functionL(x):
            return -10*sin(x)
        
        (a0, err) = quad(functionR, -1*self.period, 0) #a0 is the series constant
        (a0_, err_) = quad(functionL, 0, self.period)  
        a0 = a0 + a0_         
        self.x_0 = a0/2 * (2/self.period)           
        
        for i in range(self.depth):
            def AintegrandR(x):    
                return functionR(x)*sin(i*self.fund_freq*x)
            def AintegrandL(x):    
                return functionL(x)*sin(i*self.fund_freq*x)
            def BintegrandR(x):
                return functionR(x)*cos(i*self.fund_freq*x) 
            def BintegrandL(x):
                return functionL(x)*cos(i*self.fund_freq*x) 
            
            (ai, err) = quad(AintegrandR, -1*self.period, 0)
            (ai_,err_) = quad(AintegrandL, 0, self.period)
            ai = (2/self.period) * (ai+ai_)
            self.waves.append(ai)
            (bi, err) = quad(BintegrandR, -1*self.period, 0)
            (bi_, err_) = quad(BintegrandL, 0, self.period)
            bi = (2/self.period) * (bi+bi_)
            self.waves.append(bi) 
        return self.waves           


    def calculate(self,t):
        """ Calculates the value of the signal at time = t 
        """
        x_0 = self.x_0
        self.n = self.depth 
         
        def Sigma(x): 
            """ Uses recursion to build a signal that is evaluated at every t
            """
            if self.n == 0:
                return x_0
        
            else:
                self.n = self.n-1
                sigma = self.waves[self.n*2]*sin(self.n*self.fund_freq*t)+self.waves[self.n*2+1]*cos(self.n*self.fund_freq*t)+ Sigma(t)
                return sigma
        return Sigma(t)
                

class Canvas(object):
    """ Encodes the state of the canvas
    """
    def __init__(self, width = 17, height = 11):
        self.width = width
        self.height = height
        self.PPI = 50
        self.displayWidth = self.width * self.PPI
        self.displayHeight = self.height * self.PPI
        self.backgroundColor = (0, 0, 0)
        self.textcolor = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.displayWidth, self.displayHeight))

    def paint_parametric(self, signal1, signal2, trange = 50, width = 17, height = 11):
        """ Creates a parametric plot of signal1 vs signal2 for t = [range] where signal1 and signal2 are Signal objects
        """
        self.screen.fill(self.backgroundColor)
        for t in numpy.arange(0, 20, .1):
            x = signal1.calculate(t) * 10
            y = signal2.calculate(t) * 10
            point = Square(x + self.displayWidth/2 ,y + self.displayHeight/2,(255, 255, 255))
            point.draw(self.screen)
            pygame.display.update()
            pygame.time.wait(500)

class Marker(object):
    """ Encodes the state of markers you can plot
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = (10,10)

    def draw(self):
        pass
        #draws a marker

class Square(Marker):
    """ Encodes the state of square markers
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self. color = color
        self.size = (10,10)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, ((self.x - self.size[0]/2, self.y - self.size[1]/2),self.size),0)

def main():
    pygame.init()
    pygame.font.init()
    
    #initialize all initial objects

    signal1 = Signal(4, 1/(pi))    #set signal to depth 4 and frequency 1/pi
    signal2 = Signal(3, (1/(7*pi)))
    print signal1.waves
    signal1.build()       #Build the constants necessary for the signal
    signal2.build()
    print signal1.waves
    canvas = Canvas()      #calculate and draw the signals as coordinates
    canvas.paint_parametric(signal1, signal2)    #for now you can't quit until the program is finished drawing, so don't set a big trange. I'll fix it when I have more time

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # pygame.quit()

if __name__ == '__main__':
    main()
