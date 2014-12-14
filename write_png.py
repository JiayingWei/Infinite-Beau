import Image,math,sys,cv2
import numpy as np
from bezier import bezier

def paint_canvas(x, y, colors):
	"""creates the png file and colors colors it
	"""
	sys.setrecursionlimit(15000)
	padding = 1
	point1hat = math.atan((y[3] - y[0])/(x[3] - x[0])) + math.pi

	if x[75] - x[0] < 0:
		point1hat = math.pi + point1hat
	point2hat = math.atan((y[-1] - y[-3])/(x[-1] - x[-3]))
	if x[-1] - x[-75] < 0:
		point2hat = math.pi + point2hat

	closeIt = bezier((x[0],y[0]), point1hat, (x[-1],y[-1]), point2hat)	#calls bezier function in order to close the open loop
	xnew = x + closeIt[0]
	ynew = y + closeIt[1]

	canvas = Image.new("RGB",(int(round(max(xnew)- min(xnew)))+2*padding, int(round((max(ynew) - min(ynew))))+2*padding))
	pixels = canvas.load()

	for i in range(len(xnew)):
		pixels[xnew[i]+padding+0, ynew[i]+padding+0] = (255, 255, 255)

	imagepath = "images/techtest.png"
	canvas.save(imagepath)
	centers = findZones(imagepath)

	for i in range(len(centers)):
		flood(pixels,centers[i], color = colors[i%len(colors)], visited = [])

	canvas = canvas.resize((1000,1000), Image.NEAREST)
	canvas.save(imagepath)	

def map_coordinates(x,y, width_px = 100, height_px = 100):
	""" Maps the function to the pixel grids
	"""
	xnew = []
	ynew = []
	for i in range(len(x)):
		xnew.append(remap(x[i], min(x), max(x), 0, width_px-1))
		ynew.append(remap(y[i], min(y), max(y), 0, height_px-1))
	return xnew,ynew

def remap(value, low1, high1, low2, high2):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].
	"""
	return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

def flood(pixelgrid, (x,y), color = (255, 50, 255), background = (0,0,0), visited=[]):
	""" Recursively fills the closed contour starting at point (x,y)
	"""
	if pixelgrid[x,y] != background:
		return
	else:
		pixelgrid[x,y] = color
		visited.append((x,y))
		try:
			if (x+0,y+1) not in visited:
				flood(pixelgrid, (x+0,y+1), color = color)
			if (x+0,y-1) not in visited:
				flood(pixelgrid, (x+0,y-1), color = color)
			if ((x+1,y+0)) not in visited:
				flood(pixelgrid, (x+1,y+0), color = color)
			if ((x-1,y+0)) not in visited:	
				flood(pixelgrid, (x-1,y+0), color = color)
		except:
			pass

def findZones(imagepath):
	""" Finds the centers of each of the closed contours in the image
	"""
	image = cv2.imread(imagepath)
	imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	M = []	#moments
	centers = []
	x = []
	y = []
	
	for i in range(len(contours)):
		for j in range(len(contours[i])):
			x.append(contours[i][j][0][0])
			y.append(contours[i][j][0][1])
		leftmostX = min(x)
		centers.append((int(leftmostX + 1), int(y[x.index(leftmostX)])))
		x = []
		y = []
	return centers

def pickColor(Ak):
	"""Selects the colors of the final piece based on the input amplitudes
	"""
	red = (255,50,50)
	orange = (255,153,50)
	yellow = (255,255,50)
	green = (153,255,50)
	blue = (50,50,255)
	purple = (153,50,255)
	colors = [red,orange,yellow,green,blue,purple]
	picked = []

	for i in range(len(Ak)):
		picked.append(colors[int(remap(Ak[i], 0, max(Ak), 0, 5))])

	return picked

