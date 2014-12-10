from scipy.integrate import quad
# import matplotlib.pyplot as plt
import cmath, numpy
from math import sin as sin
from math import cos as cos
from math import pi as pi

def calculate_mu0(Ak, ak):
	"""Calculates the mu0 coefficiant from the amplitude and phase terms
	"""
	mu0 = []
	for i in range(len(Ak)):
		mu0.append(Ak[i] * cos(ak[i]))
	return sum(mu0)

def curve_generator(l,Ak,ak,mu0,L,delta0,Z0):
	"""Calculates Z(l) and returns a (x,y)
	"""
	def curve_integrate_this_real(t,Ak,ak,mu0,delta0):
		complex_number =  cmath.exp(1j * (-t + delta0 + mu0 + curve_Sigma_sum(t,Ak,ak)))
		return complex_number.real
		
	def curve_integrate_this_imag(t,Ak,ak,mu0,delta0):
		complex_number =  cmath.exp(1j * (-t + delta0 + mu0 + curve_Sigma_sum(t,Ak,ak)))
		return complex_number.imag

	def curve_Sigma_sum(t, Ak, ak):
		Sigma_sum = []
		for j in range(len(Ak)):
			Sigma_sum.append(Ak[j] * cos(j*t - ak[j]))
		return sum(Sigma_sum)

	(integral_real, erreal) = quad(func = curve_integrate_this_real, a = 0, b = 2*pi*l/L, args = (Ak,ak,mu0,delta0))
	(integral_imag, erimag) = quad(func = curve_integrate_this_imag, a = 0, b = 2*pi*l/L, args = (Ak,ak,mu0,delta0))
	integral =  integral_real + integral_imag * 1j
	integral =  L/(2*pi) * integral
	r = Z0[0] + integral
	theta = Z0[1] + integral
	return (r, theta)

def draw_curves(Ak,ak,mu0,L,delta0,Z0):
	"""Uses matlibplot to visualize the curve
	"""
	x = []
	y = []
	resolution = 2000	
	for l in numpy.arange(0,L,float(L)/resolution):
		coordinates = curve_generator(l,Ak,ak,mu0,L,delta0,Z0)
		xcomplex = coordinates[0]*cmath.cos(coordinates[1])
		ycomplex = coordinates[0]*cmath.sin(coordinates[1])
		x.append(xcomplex.real)
		y.append(ycomplex.real)
	return x,y