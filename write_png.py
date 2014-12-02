import Image
import matplotlib.pyplot as plt

def paint_canvas(x, y, width_in = 17, height_in = 11):
	PPI = 250			#pixels per inch
	width_px = PPI * width_in
	height_px = PPI * height_in
	xnew = [x + width_px-.5(max(x)-min(x)) for x in x]
	ynew = [y + .15 * height_px for y in y]

	canvas = Image.new("RGB",(width_px, height_px))
	pixels = canvas.load()

	for i in range(len(x)):
		pixels[x[i],y[i]] = (255, 255, 255)

	canvas.save("images/test1.jpg")

def map_coordinates(x,y, width_px = 17*250, height_px = 11*250):
	xnew = []
	ynew = []
	for i in range(len(x)):
		xnew.append(remap(x[i], min(x), max(x), 0, .6 * height_px))
		# xnew.append(remap(x[i], min(x), max(x), 0, .6 * height_px/(max(y) - min(y))))
		ynew.append(remap(y[i], min(y), max(y), 0, .6 * height_px))
	return xnew,ynew

def remap(value, low1, high1, low2, high2):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].
	"""
	return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

