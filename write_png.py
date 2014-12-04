import Image,math,sys
import matplotlib.pyplot as plt
from bezier import Bezier

def paint_canvas(x, y, width_in = 9, height_in = 9):
	sys.setrecursionlimit(10000)
	PPI = 250			#pixels per inch
	width_px = PPI * width_in
	height_px = PPI * height_in
	padding = 1
	point1hat = math.atan((y[75] - y[0])/(x[75] - x[0]))
	point2hat = math.atan((y[-1] - y[-75])/(x[-1] - x[-75]))

	closeIt = Bezier((x[0],y[0]), point1hat, (x[-1],y[-1]), point2hat)
	xnew = x + closeIt[0]
	ynew = y + closeIt[1]

	canvas = Image.new("RGB",(int(round(max(xnew)- min(xnew)))+2*padding, int(round((max(ynew) - min(ynew))))+2*padding))
	pixels = canvas.load()


	for i in range(len(xnew)):
		try:
			pixels[xnew[i]+padding+0,ynew[i]+padding+0] = (255, 255, 255)
			pixels[xnew[i]+padding-1,ynew[i]+padding+0] = (255, 255, 255)
			pixels[xnew[i]+padding+1,ynew[i]+padding+0] = (255, 255, 255)
			pixels[xnew[i]+padding+0,ynew[i]+padding-1] = (255, 255, 255)
			pixels[xnew[i]+padding-1,ynew[i]+padding-1] = (255, 255, 255)
			pixels[xnew[i]+padding+1,ynew[i]+padding-1] = (255, 255, 255)
			pixels[xnew[i]+padding+0,ynew[i]+padding+1] = (255, 255, 255)
			pixels[xnew[i]+padding-1,ynew[i]+padding+1] = (255, 255, 255)
			pixels[xnew[i]+padding+1,ynew[i]+padding+1] = (255, 255, 255)
		except IndexError:
			pass

	# pixels = flood(pixels, (1000,1000))

	canvas.save("images/test1.png")

def map_coordinates(x,y, width_px = 9*250, height_px = 9*250):
	xnew = []
	ynew = []
	for i in range(len(x)):
		xnew.append(remap(x[i], min(x), max(x), 0, width_px-1))
		# xnew.append(remap(x[i], min(x), max(x), 0, .6 * height_px/(max(y) - min(y))))
		ynew.append(remap(y[i], min(y), max(y), 0, height_px-1))
	return xnew,ynew

def remap(value, low1, high1, low2, high2):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].
	"""
	return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

# def flood(pixelgrid, (x,y), color = (255, 50, 255)):
# 	Q = []
# 	if pixelgrid[x,y] != (0,0,0):
# 		return
# 	Q.append((x,y))
# 	for N in Q:
# 		if pixelgrid[N[0], N[1]] == (0,0,0):
# 			w = N
# 			e = N
# 			while pixelgrid[w[0]-1, w[1]] == (0,0,0):
# 				w = (w[0]-1, w[1])
# 			while pixelgrid[e[0]+1, e[1]] == (0,0,0):
# 				e = (e[0]+1, e[1])
# 			for n in range(w[0],e[0]):
# 				pixelgrid[n,N[1]] == color
# 				if pixelgrid[n,N[1]+1] == (0,0,0):
# 					Q.append((n,N[1]+1))
# 				if pixelgrid[n,N[1]-1] == (0,0,0):
# 					Q.append((n,N[1]-1))
# 	return