import math, numpy, wave
import matplotlib.pyplot as plt
from pylab import fromstring
from math import pi 


def inputSignal(t,squishedlist, resolution = 10000):
	"""Finds the value of a signal at time t
	"""
	for i in range(int(t*resolution/(2*pi) - 5), int(t*resolution/(2*pi) + 5)):
		if squishedlist[i][0] >= t:
			return squishedlist[i][1]

def WAVtoSignal(pathname):
	"""Takes in a .wav music file and outputs its waveform
	"""
	song = wave.open(pathname,'r')
	waveform = song.readframes(-1)
	waveform = fromstring(waveform, 'Int16')
	normalized = normSignal(waveform)
	return normalized

def normSignal(waveform):
	""" Takes a waveform: normalizes the x to [-1, 1] and normalizes the y to [0, 2*pi]
	"""
	resolution = 10000					#points of resolution
	step = len(waveform)/ resolution	#step size
	squished = []						#squished waveform
	minimum = float(min(waveform))
	maximum = float(max(waveform))
	for i in range(resolution):
		squished.append([i*2*pi/resolution, float(waveform[i * step])])
		squished[i][1] = remap(squished[i][1], minimum, maximum, -1, 1)
		plt.plot(i,squished[i][1])
	plt.show()
	return squished


def remap(value, low1, high1, low2, high2):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].
	"""
	return low2 + (value - low1) * (high2 - low2) / (high1 - low1)
	# return value - low1


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
	return 0 + L/2*pi

def plotAgainstT(function, trange = 2 * pi):
	""" Takes in an input function and plots it against time. Use it for debugging
	"""
	x = []
	y = []
	for t in numpy.arange(0, trange,.1):
		x.append(t)
		y.append(function(t))
	 
	plt.plot(x, y)
	plt.show()


def plotParametric(function1, function2, trange = 2 * pi):
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

	toanyone = WAVtoSignal('comebackhome.wav')

if __name__ == '__main__':
	main()