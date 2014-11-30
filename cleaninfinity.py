import math, numpy, wave
import matplotlib.pyplot as plt
from pylab import fromstring
from scipy.integrate import quad
from math import sin as sin
from math import cos as cos
from math import pi as pi


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


def find_coeff(input_signal, depth, period):
	""" Outputs Amplitude and Phase information by Fourier transforming an input signal (which must be a function)
	"""
	def input_function(x):
		return input_signal

	fund_feq = 2 * pi / period
	AK = []
	alphaK = []

	(A0, err) = quad(func = input_function, a = 0, b = period)
	mu0 = A0 / 2

	for n in range(1, depth+1):
		def a_function(x, i):
			return input_function(x) * cos(i * fund_feq * x)
		def b_function(x, i):
			return input_function(x) * sin(i * fund_feq * x)
		(a, err) = quad(a_function, 0, period, n)
		an = 2 * a / period
		(b, err) = quad(b_function, 0, period, n)
		bn = 2 * b / period
		Ak = math.sqrt(an**2 + bn**2)
		AK.append(Ak)
		alphak = math.asin(an/Ak)
		alphaK.append(alphak)

	return (AK, alphaK, mu0, fund_feq)

def build_function(point_t):
	""" calculates the coordinate of the point at the an input time t
	"""
	coefficients = find_coeff(-1*cos(x), 2, 2*pi)
	Amp = coefficients[0]
	Phase = coefficients[1]
	constant = coefficients[2]
	fund_feq = coefficients[3]
	Sigma = []

	def find_sum(number):
		for i in range(1, len(Amp)):
			Sigma.append(Amp[i-1] * sin(i * fund_feq * number + Phase[i-1]))
		return sum(Sigma)

	return find_sum(point_t) + constant

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