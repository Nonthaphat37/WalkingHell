import pygame
from pygame.locals import *

class SimpleGame(object):
	def __init__(self, title='WalkingHell',
				background_color = pygame.Color('black'), 
				window_size=(1280, 768), 
				fps=60):

		self.title = title
		self.window_size = window_size
		self.fps = fps

		self.is_terminated = False

		self.background_color = background_color

		self.is_restart = False

		self.code = []

	def __game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace", 20)

	def run(self):
		self.__game_init()
		while not self.is_terminated:
			self.__handle_events()

			self.update()

			self.surface.fill(self.background_color)

			self.render(self.surface)

			pygame.display.update()
			self.clock.tick(self.fps)


	def terminate(self):
		self.is_terminated = True

	def restart(self):
		self.is_restart = True

	def init(self):
		pass

	def update(self):
		pass

	def render(self):
		pass

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()
			elif event.type == KEYUP and event.key == K_ESCAPE:
				self.terminate()
			elif event.type == KEYDOWN and event.key == K_r:
				self.restart()

			if len(self.code) < 4:
				if event.type == KEYUP and event.key == K_1:
					self.code.append(1)
				elif event.type == KEYUP and event.key == K_2:
					self.code.append(2)
				elif event.type == KEYUP and event.key == K_3:
					self.code.append(3)
				elif event.type == KEYUP and event.key == K_4:
					self.code.append(4)
				elif event.type == KEYUP and event.key == K_5:
					self.code.append(5)
				elif event.type == KEYUP and event.key == K_6:
					self.code.append(6)
				elif event.type == KEYUP and event.key == K_7:
					self.code.append(7)
				elif event.type == KEYUP and event.key == K_8:
					self.code.append(8)
				elif event.type == KEYUP and event.key == K_9:
					self.code.append(9)

	

	def on_key_left(self, key):
		print 'left'
 
	def on_key_right(self, key):
		print 'right'
