from scipy.integrate import quad
import math, numpy
import matplotlib.pyplot as plt

from math import sin as sin
from math import cos as cos
from math import pi as pi

def input_function(x):
	afunction = sin(x) + cos(sin(x*cos(x)))
	return afunction

def find_coeff(depth, period):
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
	return (AK, alphaK)


# print find_coeff(10, 2*pi)




# if __name__ == '__main__':
# 	def build_function(point_t):
# 		coefficients = find_coeff(15, 2*pi)
# 		Amp = coefficients[0]
# 		Phase = coefficients[1]
# 		constant = coefficients[2]
# 		fund_feq = coefficients[3]
# 		Sigma = []

# 	def find_sum(number):
# 		for i in range(1, len(Amp)):
# 			Sigma.append(Amp[i-1] * sin(i * fund_feq * number + Phase[i-1]))
# 		return sum(Sigma)

# 	return find_sum(point_t) + constant

# 	x = []
# 	y_original = []
# 	y_fourier = []

# 	for t in numpy.arange(0, 10, .1):
# 		x.append(t)
# 		thefunction = sin(t+t**2)
# 		y_original.append(thefunction)
# 		y_fourier.append(build_function(t))
# 		print (thefunction, build_function(t))

# 	plt.plot(x, y_original, label = "Original Signal")
# 	plt.plot(x, y_fourier, label = "Fourier signal")
# 	plt.legend()
# 	plt.show()