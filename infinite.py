from scipy.integrate import quad
import math, pygame

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
         self.fund_freq = 2*pi/self.period
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
        def function(x):
            return 2*x        
        
        (a0, err) =quad(function, -1*self.period, self.period) #a0 is the series constant           
        self.x_0 = a0/2 * (2/self.period)           
        
        for i in range(self.depth):
            def Aintegrand(x):    
                return function(x)*sin(i*self.fund_freq*x)
            def Bintegrand(x):
                return function(x)*cos(i*self.fund_freq*x)    
            
            (ai, err) = quad(Aintegrand, -1*self.period, self.period)
            ai = (2/self.period) * ai
            self.waves.append(ai)
            (bi, err) = quad(Bintegrand, -1*self.period, self.period)
            bi = (2/self.period) * bi
            self.waves.append(bi) 
        return self.waves            


    def calculate(self,t):
         """ Calculates the value of the signal at time = t
         """
         x_0 = self.x_0
         self.n = self.depth 
         
         def Sigma(x): 
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
		self.backgroundColor = (0, 0, 0)
		self.textcolor = (255, 255, 255)
		self.screen = pygame.display.set_mode((self.width*50, self.height*50))

	def paint_parametric(self, signal1, signal2, trange = 1000, width = 17, height = 11):
		""" Creates a parametric plot of signal1 vs signal2 for t = [range] where signal1 and signal2 are Signal objects
		"""
		self.screen.fill(self.backgroundColor)
		for t in range(trange):
			x = signal1.calculate(t)
			y = signal2.calculate(t)
   
			marker1 = Square(x,y,(255, 255, 255))
			marker1.draw(self.screen)
			pygame.display.update()



class Marker(object):
	""" Encodes the state of markers you can plot
	"""
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		self.size = (20,20)

	def draw(self):
		pass
		#draws a marker

class Square(Marker):
	""" Encodes the state of square markers
	"""
	def __init__(self, x, y, color, size = 20):
		self.x = x
		self.y = y
		self.color = color
		super(Square, self,).__init__(self.x, self.y, self.color)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, ((self.x, self.y),self.size),0)



def main():
	pygame.init()
	pygame.font.init()
	
	#initialize all initial objects

	signal1 = Signal(4, (1/pi))
	signal2 = Signal(4, (1/pi))
      signal1.build()
      signal2.build()
	canvas = Canvas()






	#build the signals using recursion

	# signal1.build()
	# signal2.build()

	# canvas.paint_parametric(signal1,signal2,)

	#loop for pygame

	########################TESTSPACE##########################


	###########################END#############################
	
	running = True

	while running:
		canvas.paint_parametric(signal1, signal2)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()

if __name__ == '__main__':
	main()
