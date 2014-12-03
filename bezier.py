import math,numpy
import matplotlib.pyplot as plt

def Bezier(point1, point1hat, point2, point2hat):
	handleLength = 300
	handle1 = (handleLength*math.cos(point1hat) + point1[0], handleLength*math.sin(point1hat) + point1[1])
	handle2 = (handleLength*math.cos(point2hat) + point2[0], handleLength*math.sin(point2hat) + point2[1])
	distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
	resolution = int(distance * 2)
	trange = range(resolution)
	h1walker = [[],[]]
	h2walker = [[],[]]
	tiewalker = [[],[]]
	l1walker = [[],[]]
	l2walker = [[],[]]
	curve = [[],[]]
	tielength = math.sqrt((handle1[0]-handle2[0])**2 + (handle1[1]-handle2[1])**2)
	tiehat = math.atan((handle2[1]-handle1[1])/(handle2[0] - handle1[0])) + math.pi
	
	for t in trange:
		h1walker[0].append(handleLength*math.cos(point1hat)*t/trange[-1] + point1[0])
		h1walker[1].append(handleLength*math.sin(point1hat)*t/trange[-1] + point1[1])
		h2walker[0].append(handleLength*math.cos(point2hat + math.pi)*t/trange[-1] + handle2[0])
		h2walker[1].append(handleLength*math.sin(point2hat + math.pi)*t/trange[-1] + handle2[1])
		tiewalker[0].append(tielength*math.cos(tiehat)*t/trange[-1] + handle1[0])
		tiewalker[1].append(tielength*math.sin(tiehat)*t/trange[-1] + handle1[1])
		######################################################################
		#problem, phi is wrong once the tiewalker moves past the h1walker
		phi1 = math.atan((tiewalker[1][-1] - h1walker[1][-1])/(tiewalker[0][-1] - h1walker[0][-1]))
		if tiewalker[0][-1] - h1walker[0][-1] < 0:
			phi1 = math.pi/2 + phi1 + math.pi/2
			if tiewalker[1][-1] - h1walker[1][-1] <0:
				phi1 = phi1 + math.pi
		phi2 = math.atan((h2walker[1][-1] - tiewalker[1][-1])/(h2walker[0][-1] - tiewalker[0][-1]))
		if h2walker[0][-1] - tiewalker[0][-1] < 0:
			phi2 = math.pi/2 + phi2 + math.pi/2
		l1wlength = math.sqrt((tiewalker[1][-1] - h1walker[1][-1])**2 + (tiewalker[0][-1] - h1walker[0][-1])**2)
		l2wlength = math.sqrt((h2walker[1][-1] - tiewalker[1][-1])**2 + (h2walker[0][-1] - tiewalker[0][-1])**2)
		l1walker[0].append(l1wlength*math.cos(phi1)*t/trange[-1] + h1walker[0][-1])
		l1walker[1].append(l1wlength*math.sin(phi1)*t/trange[-1] + h1walker[1][-1])
		l2walker[0].append(l2wlength*math.cos(phi2)*t/trange[-1] + tiewalker[0][-1])
		l2walker[1].append(l2wlength*math.sin(phi2)*t/trange[-1] + tiewalker[1][-1])
		clength = math.sqrt((l2walker[1][-1] - l1walker[1][-1])**2 + (l2walker[0][-1] - l1walker[0][-1])**2)
		angle = math.atan((l2walker[1][-1] - l1walker[1][-1])/(l2walker[0][-1] - l1walker[0][-1]))
		if l2walker[0][-1] - l1walker[0][-1] < 0:
			angle = math.pi/2 + angle + math.pi/2
		curve[0].append(clength*math.cos(angle)*t/trange[-1] + l1walker[0][-1])
		curve[1].append(clength*math.sin(angle)*t/trange[-1] + l1walker[1][-1])

	m = 98
	plt.plot(h1walker[0][m],h1walker[1][m],'ko')
	plt.plot(h2walker[0][m],h2walker[1][m],'ko')
	plt.plot(tiewalker[0][m],tiewalker[1][m],'ko')


	plt.plot(point1[0],point1[1],'ro')
	plt.plot(point2[0],point2[1],'go')
	plt.plot(handle1[0],handle1[1],'bo')
	plt.plot(handle2[0],handle2[1],'yo')
	plt.plot(h1walker[0],h1walker[1])
	plt.plot(h2walker[0],h2walker[1])
	plt.plot(tiewalker[0],tiewalker[1])
	plt.plot(l1walker[0],l1walker[1])

	plt.plot(l2walker[0],l2walker[1])
	plt.plot(curve[0],curve[1])
	plt.show()

	return curve

# point1 = (2249.0, 647.4099721530956)
# point1hat = -0.000642365473734
# point2 = (1882.9077874044585, 2032.0360834517242)
# point2hat = 0.209573311193

# closeIt = Bezier(point1, point1hat, point2 , point2hat, resolution = 100)

#point 1 is wrong/ to be specific handle1 is probably wrong...