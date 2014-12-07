import Image,sys,cv2
import numpy as np
sys.setrecursionlimit(15000)

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

image = cv2.imread("images/floodtest300a.png")
imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image2 = Image.open("images/floodtest300a.png")
if image2.mode != 'RGB':
    image2 = image.convert('RGB')

pixels = image2.load()

contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

M = cv2.moments(contours[2])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print cx,cy

flood(pixels, (cx,cy))

image2.save("images/ROAR.png")


# def zoning(image,directions):
# 	height,width = image.size
# 	pixels = image.load()
# 	zone1 = (0,0,0)
# 	zone2 = (255,50,255)
# 	zone3 = (255,255,50)
# 	zone4 = (50,255,255)
# 	zone5 = (50,50,255)
# 	white = (255,255,255)
# 	zone = [zone1,zone2,zone3,zone4]
# 	currentZone = 0

# 	for y in range(height):
# 		for x in range(width):
# 			if directions[x][y] == 'DNE':
# 				pixels[x,y] = zone[currentZone]
# 			elif directions[x][y] == 'neutral':
# 				pixels[x,y] = white
# 			elif directions[x][y] == 'CW':
# 				currentZone = currentZone + 1
# 				pixels[x,y] = white
# 			elif directions[x][y] == 'CCW':
# 				currentZone = currentZone - 1
# 				pixels[x,y] = white
# 	return pixels

			

# zoning(image)

# image.save("images/floodtest300a.png")