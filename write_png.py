import Image,math,sys
import matplotlib.pyplot as plt
from bezier import Bezier

def paint_canvas(x, y):
	sys.setrecursionlimit(15000)
	padding = 1
	point1hat = math.atan((y[3] - y[0])/(x[3] - x[0])) + math.pi
	if x[75] - x[0] < 0:
		point1hat = math.pi + point1hat
	point2hat = math.atan((y[-1] - y[-3])/(x[-1] - x[-3]))
	if x[-1] - x[-75] < 0:
		point2hat = math.pi + point2hat

	print (x[0],y[0]), point1hat, (x[-1],y[-1]), point2hat

	closeIt = Bezier((x[0],y[0]), point1hat, (x[-1],y[-1]), point2hat)
	xnew = x + closeIt[0]
	ynew = y + closeIt[1]

	canvas = Image.new("RGB",(int(round(max(xnew)- min(xnew)))+2*padding, int(round((max(ynew) - min(ynew))))+2*padding))
	pixels = canvas.load()


	for i in range(len(xnew)):
		try:
			pixels[xnew[i]+padding+0,ynew[i]+padding+0] = (255, 255, 255)
			# pixels[xnew[i]+padding-1,ynew[i]+padding+0] = (255, 255, 255)
			# pixels[xnew[i]+padding+1,ynew[i]+padding+0] = (255, 255, 255)
			# pixels[xnew[i]+padding+0,ynew[i]+padding-1] = (255, 255, 255)
			# pixels[xnew[i]+padding-1,ynew[i]+padding-1] = (255, 255, 255)
			# pixels[xnew[i]+padding+1,ynew[i]+padding-1] = (255, 255, 255)
			# pixels[xnew[i]+padding+0,ynew[i]+padding+1] = (255, 255, 255)
			# pixels[xnew[i]+padding-1,ynew[i]+padding+1] = (255, 255, 255)
			# pixels[xnew[i]+padding+1,ynew[i]+padding+1] = (255, 255, 255)
		except IndexError:
			pass

	# pixels = flood(pixels, (1000,1000))
	canvas = canvas.resize((1000,1000), Image.NEAREST)
	canvas.save("images/test1.png")

def map_coordinates(x,y, width_px = 100, height_px = 100):
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

