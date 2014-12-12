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
	def __init__(self, model, controller):
		self.model = model
		self.controller = controller

	def drawPrompt(self):
		self.model.state = 'prompt'

		self.screen = pygame.display.set_mode((self.model.width, self.model.height),pygame.FULLSCREEN)
		self.screen.fill(self.model.background)

		micPic = pygame.image.load('GUIimages/infinitebeaumic.jpg')
		self.screen.blit(micPic,((self.model.width - micPic.get_width())/2 , (self.model.height - micPic.get_height())/2))
		pygame.display.update()

	def drawRecording(self):
		self.model.state = 'recording'
		
		self.screen.fill(self.model.background)
		recPic = pygame.image.load('GUIimages/recording.jpg')
		self.screen.blit(recPic,((self.model.width - recPic.get_width())/2 , (self.model.height - recPic.get_height())/5))

		pygame.display.update()
		# pygame.time.wait(1000)

		five = pygame.image.load('GUIimages/five.jpg')
		four = pygame.image.load('GUIimages/four.jpg')
		three = pygame.image.load('GUIimages/three.jpg')
		two = pygame.image.load('GUIimages/two.jpg')
		one = pygame.image.load('GUIimages/one.jpg')

		count = (five,four,three,two,one)

		for number in count:
			self.screen.blit(number,((self.model.width - number.get_width())/2 , (self.model.height - number.get_height())/1.5))
			pygame.display.update()
			pygame.time.wait(1000)

		self.drawLoading()

	def drawLoading(self):
		self.model.state = 'loading'

		self.screen.fill(self.model.background)
		dot = pygame.image.load('GUIimages/dot.jpg')
		dotdot = pygame.image.load('GUIimages/dotdot.jpg')
		dotdotdot = pygame.image.load('GUIimages/dotdotdot.jpg')

		loading = (dot, dotdot, dotdotdot)

		process1 = Process(target = infinite.main)
		process1.start()

		def loadingscreen():
			running = 1
			while running:
				for dot in loading:
					self.screen.blit(dot,((self.model.width - dot.get_width())/2 , (self.model.height - dot.get_height())/2))
					pygame.display.update()
					pygame.time.wait(1000)


		process2 = Process(target = loadingscreen)
		process2.start()


		pygame.time.wait(1000)

		if infinite.main() == False:
			loadingscreen. running = 0
			self.drawComplete()

	def drawComplete(self):
		self.model.state = 'complete'

		self.screen.fill((0,0,0))
		masterpiece = pygame.image.load('images/techtest.png')
		masterpiece = pygame.transform.scale(masterpiece, (model.height - 100, model.height - 100))
		redo = pygame.image.load('GUIimages/redo.png')
		redo = pygame.transform.scale(redo, (100,100))
		
		self.screen.blit(masterpiece,((self.model.width - masterpiece.get_width())/2 , (self.model.height - masterpiece.get_height())/1.5))
		self.screen.blit(redo,(self.model.width - 150 , self.model.height - 150))
		pygame.display.update()
		# return False

class Controller:
	"""Encodes Controller
	"""
	def __init__(self,model):
		self.model = model


if __name__ == '__main__':
	pygame.init()


	model = Model()
	controller = Controller(model)
	view = View(model,controller)

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
				process1 = Process(target = view.drawRecording)
				process1.start()

				process2 = Process(target = audio_record.record(5, "Audio/recordtest.wav"))
				process2.start()

			if event.type == pygame.MOUSEBUTTONDOWN and model.state == 'complete':
				(mousex,mousey) = pygame.mouse.get_pos()
				if mousex > model.width - 150  and mousex < model.width - 50 and mousey > model.height - 150 and mousey < model.height - 50:
					view.drawPrompt()
		# if model.state == 'loading':
		# 		view.drawLoading()



		#if the image has finished processing then
		#model.state = 'complete'

	pygame.quit()
