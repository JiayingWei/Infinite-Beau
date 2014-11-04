import math

class wave(object):
	""" Creates a wave object
	"""
	def __init__(self, amplitude = 1, frequency, phase):
		self.amplitude = amplitude
		self.frequency = frequency
		self.period = 1/frequency
		self.phase = phase

class signal(object):
	""" Creates a signal comprised of many waves (so an approximate of a signal)
	"""
	def __init__(self, depth):
		self.depth = depth
		self.waves = []	#list of wave objects

	def build_signal(self,list, depth):
		""" Uses recursion to create a approximation of a n depth signal
		""" 
		#if basecase == true quit
			#return base wave
		#calculate the nth wave
		nthwave = wave(1,1,1)
		self.waves.append(build_signal(self.waves, depth-1))
		return nthwave

def parametric(signal1, signal2, range, width = 17, height = 11):
	""" Creates a parametric plot of signal1 vs signal2 for t = [range]
	"""
	for t in range:
		x = signal1(t)
		y = signal2(t)
		#draw dot/square


def main():
	# build signal 1
	# build signal 2
	# plot signals

if __name__ == '__main__':
	main()