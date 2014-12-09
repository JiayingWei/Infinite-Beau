from scipy.integrate import quad
import math, numpy, wave
import input_waves
from pylab import fromstring

from math import sin as sin
from math import cos as cos
from math import pi as pi


def input_function(given_x):
	""" find the input signal's corresponding value of the argument x using
	the signal_Assignment dictionary argument. 
	This function is used to help with the successful integration of the signal
	for Foruier calculation usage.
	"""
	keys = signal_Assignment.keys()
	keys.sort

	for i in range(len(signal_Assignment)):
		if given_x > keys[-1]:
			return signal_Assignment[keys[-1]]
		elif given_x > keys[i] and given_x < keys[i+1]:
			if given_x < (keys[i]+keys[i+1])/2:
				return signal_Assignment[keys[i]]
			else:
				return signal_Assignment[keys[i+1]]
		elif given_x == keys[i]:
			return signal_Assignment[keys[i]]

	
def signal_dictionary():
	""" Create a dictionary of the corresponding x and y
	values of the normalized input wave signal
	"""
	x = []
	y = []
	assign_points = {}

	signal = input_waves.WAVtoSignal("comebackhome.wav")
	for i in range(len(signal)):
		x = signal[i][0]
		y = signal[i][1]
		assign_points.update({x:y})
	print 'assign dictionary complete'
	return assign_points

def find_coeff(depth, period = 2*pi):
	""" Calculate the Fourier coefficients approximately describing the 
	input_function to the accuracy of the given depth and period
	A maximum depth of no more than 12 is highly recommended.
	"""
	fund_feq = 2 * pi / period
	AK = []
	alphaK = []

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
	return (AK, alphaK)
