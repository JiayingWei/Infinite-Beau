from multiprocessing import Process
import pygame
import audio_record
import infinite

class Model:
	"""Encodes model state
	"""
	def __init__(self):
		self.states = ['prompt','recording','loading','complete']
		self.state = 'prompt'
		self.resolution = pygame.display.Info()
		self.width = self.resolution.current_w
		self.height = self.resolution.current_h
		self.background = (255,255,255)

class View:
	"""Encodes view state
	"""
	def __init__(self, model):
		self.model = model

	def drawPrompt(self):
		"""Displays the initial infinite beau screen
		"""
		self.model.state = 'prompt'

		self.screen = pygame.display.set_mode((self.model.width, self.model.height),pygame.FULLSCREEN)
		self.screen.fill(self.model.background)

		micPic = pygame.image.load('GUIimages/infinitebeaumic.jpg')
		self.screen.blit(micPic,((self.model.width - micPic.get_width())/2 , (self.model.height - micPic.get_height())/2))
		pygame.display.update()

	def drawRecording(self):
		"""Displays the countdown and recording screen also starts recording
		"""
		self.screen.fill(self.model.background)
		recPic = pygame.image.load('GUIimages/recording.jpg')
		# self.screen.blit(recPic,((self.model.width - recPic.get_width())/2 , (self.model.height - recPic.get_height())/5))

		pygame.display.update()

		five = pygame.image.load('GUIimages/five.jpg')
		four = pygame.image.load('GUIimages/four.jpg')
		three = pygame.image.load('GUIimages/three.jpg')
		two = pygame.image.load('GUIimages/two.jpg')
		one = pygame.image.load('GUIimages/one.jpg')

		count = (three,two,one)

		for number in count:
			self.screen.blit(number,((self.model.width - number.get_width())/2 , (self.model.height - number.get_height())/1.5))
			pygame.display.update()
			pygame.time.wait(1000)

		self.screen.fill(self.model.background)
		self.screen.blit(recPic,((self.model.width - recPic.get_width())/2 , (self.model.height - number.get_height())/1.5))		
		pygame.display.update()
		self.model.state = 'loading'

	def drawLoading(self):
		"""Displays the loading screen while infinite.py processes the waveform and turns it into a PNG file
		"""
		self.screen.fill(self.model.background)
		dot = pygame.image.load('GUIimages/dot.jpg')
		dotdot = pygame.image.load('GUIimages/dotdot.jpg')
		dotdotdot = pygame.image.load('GUIimages/dotdotdot.jpg')

		loading = (dot, dotdot, dotdotdot)
		calculating = Process(target = infinite.main)
		calculating.start()

		while calculating.is_alive() == True:
			for dot in loading:
				self.screen.blit(dot,((self.model.width - dot.get_width())/2 , (self.model.height - dot.get_height())/2))
				pygame.display.update()
				pygame.time.wait(1000)

		self.model.state = 'complete'
		view.drawComplete()

	def drawComplete(self):
		"""Displays the finished interperated PNG from the waveform
		"""

		self.screen.fill((0,0,0))
		masterpiece = pygame.image.load('images/techtest.png')
		masterpiece = pygame.transform.scale(masterpiece, (model.height - 100, model.height - 100))
		redo = pygame.image.load('GUIimages/redo.png')
		redo = pygame.transform.scale(redo, (100,100))
		
		self.screen.blit(masterpiece,((self.model.width - masterpiece.get_width())/2 , (self.model.height - masterpiece.get_height())/1.5))
		self.screen.blit(redo,(self.model.width - 150 , self.model.height - 150))
		pygame.display.update()

if __name__ == '__main__':
	pygame.init()

	model = Model()
	view = View(model)

	running = True
	view.drawPrompt()


	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN and model.state == 'prompt':
				model.state = 'recording'
				counting = Process(target = view.drawRecording())
				counting.start()
				recording = Process(target = audio_record.record())
				recording.start()
				
			if event.type == pygame.MOUSEBUTTONDOWN and model.state == 'complete':
				(mousex,mousey) = pygame.mouse.get_pos()
				if mousex > model.width - 150  and mousex < model.width - 50 and mousey > model.height - 150 and mousey < model.height - 50:
					model.state = 'prompt'
					view.drawPrompt()
		if model.state == 'loading':
			view.drawLoading()
	pygame.quit()
