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

	closeIt = Bezier((x[0],y[0]), point1hat, (x[-1],y[-1]), point2hat)
	xnew = x + closeIt[0]
	ynew = y + closeIt[1]

	canvas = Image.new("RGB",(int(round(max(xnew)- min(xnew)))+2*padding, int(round((max(ynew) - min(ynew))))+2*padding))
	pixels = canvas.load()

	direction = []	#direction in which the curve is being drawn
	for x in range(int(round(max(xnew) + padding))):
		direction.append([])
		for y in range(int(round(max(ynew) + padding))):
			direction[x].append('DNE')	#Does not exist

	#makes the drawn pixels a certain color and then labels its direction

	for i in range(len(xnew)):
		pixels[xnew[i]+padding+0, ynew[i]+padding+0] = (255, 255, 255)
		if i == 1:
			if round(ynew[1]) > round(ynew[0]):
				direction[int(round(xnew[i]+padding-1))][int(round(ynew[i]+padding-1))] = 'CCW'
			elif round(ynew[1]) < round(ynew[0]):
				direction[int(round(xnew[i]+padding-1))][int(round(ynew[i]+padding-1))] = 'CW'
			elif round(ynew[1]) == round(ynew[0]):
				direction[int(round(xnew[i]+padding-1))][int(round(ynew[i]+padding-1))] = 'neutral'
		elif round(ynew[i-1]) < round(ynew[i]) :
			direction[int(round(xnew[i]+padding-1))][int(round(ynew[i]+padding-1))] = 'CCW'	
		elif round(ynew[i-1]) > round(ynew[i]):
			direction[int(round(xnew[i]+padding-1))][int(round(ynew[i]+padding-1))] = 'CW'
		elif round(ynew[i-1]) == round(ynew[i]):
			direction[int(round(xnew[i]+padding-1))][int(round(ynew[i]+padding-1))] = 'neutral'

	# pixels = flood(pixels, (50,50))

	# print canvas.size
	# print len(direction), len(direction[0])

	pixels = zoning(canvas, direction)

	canvas = canvas.resize((1000,1000), Image.NEAREST)
	canvas.save("images/test1.png")

def map_coordinates(x,y, width_px = 100, height_px = 100):
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

def flood(pixelgrid, (x,y), background = (0,0,0), color = (255, 50, 255), visited=[]):
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

def zoning(image,directions):
	height,width = image.size
	pixels = image.load()
	white = (255,255,255)
	zone = [(0,0,0),(255,50,255),(255,255,50),(50,50,255),(255,255,255),(255,50,50),(50,255,50)]
	currentZone = 0

	for y in range(len(directions[1])):
		try:
			for x in range(len(directions)):
				if directions[x][y] == 'DNE':
					pixels[x,y] = zone[currentZone]
				elif directions[x][y] == 'neutral':
					pixels[x,y] = white
				elif directions[x][y] == 'CW':
					print directions[x][y]
					currentZone = currentZone + 1
					pixels[x,y] = white
				elif directions[x][y] == 'CCW':
					currentZone = currentZone - 1
					pixels[x,y] = white
		except:
			pass
	return pixels