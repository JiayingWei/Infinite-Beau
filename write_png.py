import Image,math
import matplotlib.pyplot as plt
from bezier import Bezier

def paint_canvas(x, y, width_in = 9, height_in = 9):
	PPI = 250			#pixels per inch
	width_px = PPI * width_in
	height_px = PPI * height_in
	padding = 3 * PPI
	canvas = Image.new("RGB",(width_px+2*padding, height_px+2*padding))
	pixels = canvas.load()

	point1hat = math.atan((y[0] - y[1])/((x[0] - x[1])))
	point2hat = math.atan((y[-1] - y[-2])/((x[-1] - x[-2])))

	print (x[0],y[0])
	print point1hat
	print (x[-1],y[-1])
	print point2hat
	closeIt = Bezier((x[0],y[0]), point1hat, (x[-1],y[-1]), point2hat, resolution = 100)
	xnew = x + closeIt[0]
	ynew = y + closeIt[1]

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

	canvas.save("images/test1.jpg")

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

