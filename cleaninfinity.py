import math, numpy
import matplotlib.pyplot as plt


def inputsignal(t):
	return math.sin(t)


def fourierTransform(input_signal, depth):
	""" Outputs Amplitude and Phase information by Fourier transforming an input signal (which must be a function)
	"""
	amplitude = []
	phi = []

	return [amplitude, phi]

def calculateCurve(amplitude, phi, t):
	""" Takes in the Amplitude and Phi information of the Fourier transform of the input signal
		and outputs the value of the calculated curve at a time t
	"""
	return 0 + L/2*math.pi

def plotAgainstT(function, trange = 2 * math.pi):
	""" Takes in an input function and plots it against time. Use it for debugging
	"""
	x = []
	y = []
	for t in numpy.arange(0, trange,.1):
		x.append(t)
		y.append(function(t))
	 
	plt.plot(x, y)
	plt.show()


def plotParametric(function1, function2, trange = 2 * math.pi):
	""" Takes in an input function and plots it parametrically against SOMETHING
	"""
	x = []
	y = []

	for t in numpy.arange(0, trange,.1):
		x.append(function1(t))
		y.append(function2(t))
	plt.plot(x, y)
	plt.show()

def main():
	""" Body runs here
	"""
	plotAgainstT(inputsignal)

if __name__ == '__main__':
	main()