import math, numpy, wave
import matplotlib.pyplot as plt
from pylab import fromstring


def inputsignal(t):
	return math.sin(t)


def WAVtoSignal(pathname):
	"""Takes in a .wav music file and outputs its waveform
	"""
	song = wave.open(pathname,'r')
	waveform = song.readframes(-1)
	waveform = fromstring(waveform, dtype = int)
	return waveform

def normSignal(waveform):
	""" Takes a waveform: normalizes the x to [-1, 1] and normalizes the y to [0, 2*pi]
	"""
	resolution = 10000					#points of resolution
	step = len(waveform)/ resolution	#step size
	squished = []						#squished waveform
	minimum = min(waveform)
	maximum = max(waveform)
	for i in range(resolution):
		squished.append(waveform[i * step])
		squished[i] = remapInterval(squished[i], minimum, maximum, -1, 1)
	plt.plot(squished)
	plt.show()
	return squished


def remapInterval(value, input_start, input_end, output_start, output_end):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].
	"""
	return (value - input_start) * (output_end - output_start) / (input_end - input_start) + output_start


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
	duck = WAVtoSignal('comebackhome.wav')
	normSignal(duck)	
if __name__ == '__main__':
	main()