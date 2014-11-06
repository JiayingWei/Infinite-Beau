import math, pygame

class Wave(object):
	""" Creates a wave object
	"""
	def __init__(self, amplitude, frequency, phase):
		self.amplitude = amplitude
		self.frequency = frequency
		self.period = 1/frequency
		self.phase = phase

class Signal(object):
	""" Creates a signal comprised of many waves (so an approximate of a signal)
	"""
	def __init__(self, depth):
		self.depth = depth
		self.waves = []	#list of wave objects

	def build(self,list, depth):
		""" Uses recursion to create a approximation of a n depth signal (probably has to return a list which has to be turned into an equation in calculate)
		""" 
		#if basecase == true quit
			#return base wave
		#calculate the nth wave
		nthwave = wave(1,1,1)
		self.waves.append(build_signal(self.waves, depth-1))
		return nthwave

	def calculate(self,t):
		""" Calculates the value of the signal at time = t
		"""
		return 5

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

	signal1 = Signal(4)
	signal2 = Signal(4)
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