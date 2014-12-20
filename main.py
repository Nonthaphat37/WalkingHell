import pygame
from pygame.locals import *
from gamelib import SimpleGame
from player import Player
from management import *
from platform import *
from gameobject import *

class WalkingHell(SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	pos_Player = (100, 468)	
	pos_Floor = ((0, 468),(1100, 250),(1750, 168),(2300, -28),(3150, -28),(3250, 350),(3700, 168),(4300, 173),(5000, 168),(5600, 318),(5900, 168),(6400, -532),(6350, -578),(7100, 168),(7700, 168),(8400,200))
	pos_Box = ((1200, 368),(1180, 150),(2100, 268),(2450, -168),(2750, -168),(4000, 68),(8000, 0))
	pos_Thorn = ((5600, 318),(5620, 318),(5640, 318),(5660, 318),(5680, 318),(5700, 318),(5720, 318),(5740, 318),(5760, 318),(5780, 318),(5800, 318),(5820, 318),(5840, 318),(5860, 318),(5880, 318))

	def __init__(self):
		super(WalkingHell, self).__init__(background_color = WalkingHell.BLACK)
		self.player = Player(pos=WalkingHell.pos_Player)
		self.controller = Controller()
		self.platform = [Floor(pos=WalkingHell.pos_Floor[0], weight=1750, height=300, color = pygame.Color('blue')),
						Floor(pos=WalkingHell.pos_Floor[1], weight=350, height=40, color = pygame.Color('red')),
						Floor(pos=WalkingHell.pos_Floor[2], weight=1400, height=600, color = pygame.Color('green')),
						Floor(pos=WalkingHell.pos_Floor[3], weight=660, height=40, color = pygame.Color('white')),
						Floor(pos=WalkingHell.pos_Floor[4], weight=100, height=800, color = pygame.Color('yellow')),
						Floor(pos=WalkingHell.pos_Floor[5], weight=450, height=600, color = pygame.Color('grey')),
						Floor(pos=WalkingHell.pos_Floor[6], weight=600, height=600, color = pygame.Color('purple')),
						FloorSlide(pos=WalkingHell.pos_Floor[7], weight=300, height=40, color = pygame.Color('red'), range_x1 = 4300, range_x2 = 5000),
						Floor(pos=WalkingHell.pos_Floor[8], weight=600, height=600, color = pygame.Color('green')),
						Floor(pos=WalkingHell.pos_Floor[9], weight=300, height=500, color = pygame.Color('blue')),
						Floor(pos=WalkingHell.pos_Floor[10], weight=1200, height=600, color = pygame.Color('grey')),
						Door(pos=WalkingHell.pos_Floor[11], weight=50, height=700, color = pygame.Color('grey'), thick = 0, correctCode = [1,1,1,2]),
						Floor(pos=WalkingHell.pos_Floor[12], weight=150, height=600, color = pygame.Color('white'), thick = 0),
						FloorSlide(pos=WalkingHell.pos_Floor[13], weight=300, height=40, color = pygame.Color('red'), range_x1 = 7100, range_x2 = 7700),
						Floor(pos=WalkingHell.pos_Floor[14], weight=700, height=600, color = pygame.Color('blue')),
						FloorSlide(pos=WalkingHell.pos_Floor[15], weight=300, height=40, color = pygame.Color('red'), range_x1 = 8400, range_x2 = 9100),]


		self.thorn = [Thorn(WalkingHell.pos_Thorn[0]),
					Thorn(WalkingHell.pos_Thorn[1]),
					Thorn(WalkingHell.pos_Thorn[2]),
					Thorn(WalkingHell.pos_Thorn[3]),
					Thorn(WalkingHell.pos_Thorn[4]),
					Thorn(WalkingHell.pos_Thorn[5]),
					Thorn(WalkingHell.pos_Thorn[6]),
					Thorn(WalkingHell.pos_Thorn[7]),
					Thorn(WalkingHell.pos_Thorn[8]),
					Thorn(WalkingHell.pos_Thorn[9]),
					Thorn(WalkingHell.pos_Thorn[10]),
					Thorn(WalkingHell.pos_Thorn[11]),
					Thorn(WalkingHell.pos_Thorn[12]),
					Thorn(WalkingHell.pos_Thorn[13]),
					Thorn(WalkingHell.pos_Thorn[14])]


		self.gameobject = [Stone(WalkingHell.pos_Box[0], 100, 100), Stone(WalkingHell.pos_Box[1], 100, 100), Stone(WalkingHell.pos_Box[2], 100, 100), 
					Stone(WalkingHell.pos_Box[3], 100, 100), Stone(WalkingHell.pos_Box[4], 100, 100), Stone(WalkingHell.pos_Box[5], 100, 100), Stone(WalkingHell.pos_Box[6], 100, 200)]
		
		cameraOffset = [float(self.window_size[0])/3, float(self.window_size[1])/2]
		self.camera = Camera(offset = cameraOffset)

		self.player_Height = self.player.player_Height
		self.player_Weight = self.player.player_Weight



	def init (self):
		super(WalkingHell, self).init()
		
	def update(self):

		super(WalkingHell, self).update()
		self.controller.controllerPlayer(self.player)
		self.player.update()
		self.controller.updateStatePlayer(self.player)
		if self.controller.collisionEngine(self.player, self.platform, self.gameobject, self.thorn):
			self.is_restart = True

		#------------------------------RestartGame---------------------------------------#
		self.restartGame()

		self.camera.update(playerPosition = [self.player.x, self.player.y])
		for i in range(len(self.gameobject)):
			self.gameobject[i].update()
		for i in range(len(self.platform)):
			if type(self.platform[i]).__name__ == 'Door':
				if self.controller.collisionPlayerinIphone(self.player, self.platform[i]):
					self.platform[i].checkCollisionToCode(True)
					self.platform[i].update(code = self.code)
				else:
					self.platform[i].checkCollisionToCode(False)
					self.platform[i].update(code = [])
			else:
				self.platform[i].update()


		if len(self.code) > 3:
			self.code = []


		if self.player.y > 1700 :
			self.is_restart = True



	def restartGame(self):
		if self.is_restart:
			#---restart player---#
			self.player.x = WalkingHell.pos_Player[0]
			self.player.y = WalkingHell.pos_Player[1]-300

			#---restart gameobject---#
			for i in range(len(self.gameobject)):
				self.gameobject[i].x = WalkingHell.pos_Box[i][0]
				self.gameobject[i].y = WalkingHell.pos_Box[i][1]

			#---restart platform---#
			for i in range(len(self.platform)):
				if type(self.platform[i]).__name__ == 'Door':
					self.platform[i].is_correctCode = False
			self.code = []

			self.setRestartGame()

	def setRestartGame(self):
		self.is_restart = False


	def render(self, surface):
		super(WalkingHell, self).render()
		self.renderThorn(surface)
		for i in range(len(self.gameobject)):
			self.gameobject[i].render(surface, posUpdate = self.camera.position)
		self.renderPlatform(surface)
		self.player.render(surface, posUpdate = self.camera.position)

	def renderPlatform(self, surface):
		for i in range(len(self.platform)):
			self.platform[i].render(surface, camPos = self.camera.position)

	def renderThorn(self, surface):
		for i in range(len(self.thorn)):
			self.thorn[i].render(surface, posUpdate = self.camera.position)

def main():
	game = WalkingHell()
	game.run()

if __name__ == '__main__':
	main()
