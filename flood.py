import Image,sys
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

image = Image.open("images/floodtest300.png")
if image.mode != 'RGB':
    image = image.convert('RGB')
pixels = image.load()
flood(pixels, (200,200), visited = [])

image.save("images/floodtest300a.png")

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