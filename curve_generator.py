from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import cmath
from math import sin as sin
from math import cos as cos
from math import pi as pi

"""How is x and y different? It seems like the only way x and y are different are calculated from the Z0 initial starting conditions
"""

def calculate_mu0(Ak, ak):
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
	x = Z0[0] + integral
	y = Z0[1] + integral
	return (x,y)

def draw_curves(Ak,ak,mu0,L,delta0,Z0):
	x = []
	y = []	
	for l in range(0,L,L/10):
		coordinates = curve_generator(l,Ak,ak,mu0,L,delta0,Z0)
		x.append(coordinates[0])
		y.append(coordinates[1])
	plt.plot(x,y)
	plt.show()

def main():
	#What is being outputted from the FFT function?
	#A list of [Ak] and a list of [ak]
	#The depth would be the length of Ak
	Ak = [1,2,3,4]
	ak = [4,3.3,2,1]
	mu0 = calculate_mu0(Ak,ak)

	L = 10 #length of the line
	delta0 = 1 #no idea what units this should be in
	Z0 = (0,0) #not sure if this is right

	draw_curves(Ak,ak,mu0,L,delta0,Z0)
	
if __name__ == '__main__':
	main()
# fourier_descriptors = [Ak, ak, mu0]	#Ak is the amplitude of the forier series, and ak is the phase shift, mu0 = sum of 
# triple = [L, delta0, Z0]	#repressents [length, initial tangential direction, position of starting point]

# def curve_generator([Ak][][])