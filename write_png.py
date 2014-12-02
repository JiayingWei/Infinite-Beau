import Image
import matplotlib.pyplot as plt

def paint_canvas(x, y, width_in = 9, height_in = 9):
	PPI = 250			#pixels per inch
	width_px = PPI * width_in
	height_px = PPI * height_in
	xnew = x
	ynew = y
	canvas = Image.new("RGB",(width_px+2, height_px+2))
	pixels = canvas.load()

	for i in range(len(xnew)):
		pixels[xnew[i]+1,ynew[i]+1] = (255, 255, 255)
		pixels[xnew[i]+0,ynew[i]+1] = (255, 255, 255)
		pixels[xnew[i]+2,ynew[i]+1] = (255, 255, 255)
		pixels[xnew[i]+1,ynew[i]+0] = (255, 255, 255)
		pixels[xnew[i]+0,ynew[i]+0] = (255, 255, 255)
		pixels[xnew[i]+2,ynew[i]+0] = (255, 255, 255)
		pixels[xnew[i]+1,ynew[i]+2] = (255, 255, 255)
		pixels[xnew[i]+0,ynew[i]+2] = (255, 255, 255)
		pixels[xnew[i]+2,ynew[i]+2] = (255, 255, 255)

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

