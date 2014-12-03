def inputSignal(t,squishedlist, resolution = 100000):
	"""Finds the value of a signal at time t
	"""
	for i in range(int(t*resolution/(2*pi) - 5), int(t*resolution/(2*pi) + 5)):
		if squishedlist[i][0] >= t:
			return squishedlist[i][1]

def WAVtoSignal(pathname):
	"""Takes in a .wav music file and outputs its waveform
	"""
	song = wave.open(pathname,'r')
	waveform = song.readframes(-1)
	waveform = fromstring(waveform, 'Int16')
	normalized = normSignal(waveform)
	return normalized

def normSignal(waveform):
	""" Takes a waveform: normalizes the x to [-1, 1] and normalizes the y to [0, 2*pi]
	"""
	resolution = 10000					#points of resolution
	step = len(waveform)/ resolution	#step size
	squished = []						#squished waveform
	minimum = float(min(waveform))
	maximum = float(max(waveform))
	for i in range(resolution):
		squished.append([i*2*pi/resolution, float(waveform[i * step])])
		squished[i][1] = remap(squished[i][1], minimum, maximum, -1, 1)
		plt.plot(i,squished[i][1])
	plt.show()
	return squished


def remap(value, low1, high1, low2, high2):
	""" Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].
	"""
	return low2 + (value - low1) * (high2 - low2) / (high1 - low1)
