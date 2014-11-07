from scipy.integrate import quad
import math

pi = math.pi

def sin(x):
      return math.sin(x)
def cos(x):
      return math.cos(x)

class wave(object):
	""" Creates a wave object
	"""
	def __init__(self, amplitude = 1, frequency, phase):
		self.amplitude = amplitude
		self.frequency = frequency
		self.period = 1/frequency
            self.fund_freq = 2*pi/self.period
		self.phase = phase


class signal(wave):
	""" Creates a signal comprised of many waves (so an approximate of a signal)
	"""
	def __init__(self, depth):
		self.depth = depth #          N = #define depth
		self.waves = []	#list of wave objects
                        
      def function(self, equation):
            return equation

      def build_signal(self,list):
		""" Uses recursion to create a approximation of a n depth signal
		""" 
            a0, err = (2/self.period)*quad(function(equation), -1*self.period, self.period)            
            self.x_0 = a0/2            
            n = self.depth
            
            for i in range(self.depth):
                def Aintegrand(x):    
                    return function(x)*sin(i*w0*x)
                def Bintegrand(x):
                    return function(x)*cos(i*w0*x)    
                
                ai, err = (2/period)*quad(Aintegrand, -1*period, period)
                self.waves.append(ai)
                bi, err = (2/period)*quad(Bintegrand, -1*period, period)     
                self.waves.append(bi)    
            return self.waves            

                    
#		nthwave = wave(1,1,1) #?
#		self.waves.append(build_signal(self.waves, self.depth-1))
#		return nthwave

def parametric(signal1, signal2, range, width = 17, height = 11):
	""" Creates a parametric plot of signal1 vs signal2 for t = [range]
	"""
      x_0 = signal.build_signal.x_0
	for t in range:
     
         def Sigma(x):    
            if n == 0:
                return x_0
        
            else:
                n = n-1
                sigma = self.waves[n*2]*sin(n*w0*t)+self.waves[n*2+1]*cos(n*w0*t)+ Sigma(t)
                return sigma
                
		x = Sigma(t)
		y = Sigma(t)
		#draw dot/square


def main():
	# build signal 1
	# build signal 2
	# plot signals

if __name__ == '__main__':
	main()