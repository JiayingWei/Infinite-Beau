import Image,sys

image = Image.open("images/test1.png")
if image.mode != 'RGB':
    image = image.convert('RGB')

def zoning(image,directions):
	height,width = image.size
	pixels = image.load()
	zone1 = (0,0,0)
	zone2 = (255,50,255)
	zone3 = (255,255,50)
	zone4 = (50,255,255)
	zone5 = (50,50,255)
	white = (255,255,255)
	zone = [zone1,zone2,zone3,zone4]
	currentZone = 0

	for y in range(height):
		for x in range(width):
			if directions[x][y] == 'DNE':
				pixels[x,y] = zone[currentZone]
			elif directions[x][y] == 'neutral':
				pixels[x,y] = white
			elif directions[x][y] == 'CW':
				currentZone = currentZone + 1
				pixels[x,y] = white
			elif directions[x][y] == 'CCW':
				currentZone = currentZone - 1
				pixels[x,y] = white
	return pixels

			

zoning(image)

# image.save("images/floodtest300a.png")