import pygame
from pygame.locals import *

class GameObject(object):
	G = -1
	def __init__(self, pos, weight, height):
		(self.x, self.y) = pos
		(self.vy, self.vx) = (0, 0)
		(self.svx, self.svy) = pos
		self.gameobject_Weight = weight
		self.gameobject_Height = height
		self.rectgameobject = pygame.Rect(self.x, self.y, self.gameobject_Weight, self.gameobject_Height)
		self.vx_onPlatform = 0

		self.rect_ErrorSize = 1
		self.rect_ErrorPosition = 10
		self.rect_Weight = self.gameobject_Weight-self.rect_ErrorPosition*2
		self.rect_Height = self.gameobject_Height-self.rect_ErrorPosition*2

		self.pos_rectUpdate()

		self.colDown = False
		self.colUp = False
		self.colLeft = False
		self.colRight = False

	def update(self):
		self.x = self.x + self.vx + self.vx_onPlatform
		self.updateGravity()
		self.pos_rectUpdate()
		self.rectgameobject = pygame.Rect(self.x, self.y, self.gameobject_Weight, self.gameobject_Height)

	def updateGravity(self):
		self.y -= self.vy
		self.vy += GameObject.G

	def render(self):
		pass

	def pos_rectUpdate(self):
		self.rectgameobject_weightLeft = pygame.Rect(self.x, 
												self.y+self.rect_ErrorPosition, 
												self.rect_ErrorSize, 
												self.rect_Height)
		self.rectgameobject_weightRight = pygame.Rect(self.x+self.gameobject_Weight, 
												self.y+self.rect_ErrorPosition,
												self.rect_ErrorSize, 
												self.rect_Height)
		self.rectgameobject_heightUp = pygame.Rect(self.x+self.rect_ErrorPosition, 
												self.y,
												self.rect_Weight, 
												self.rect_ErrorSize)
		self.rectgameobject_heightDown = pygame.Rect(self.x+self.rect_ErrorPosition, 
												self.y+self.gameobject_Height+self.rect_ErrorSize, 
												self.rect_Weight, 
												self.rect_ErrorSize)

class Stone(GameObject):
	def __init__(self, pos, weight, height):
		super(Stone, self).__init__(pos, weight, height)


	def render(self, surface, posUpdate):
		
		# tempLeftRect = pygame.Rect( self.rectgameobject_weightLeft.left - posUpdate[0], self.rectgameobject_weightLeft.top - posUpdate[1], self.rectgameobject_weightLeft.width, self.rectgameobject_weightLeft.height )
		# tempRightRect = pygame.Rect( self.rectgameobject_weightRight.left - posUpdate[0], self.rectgameobject_weightRight.top - posUpdate[1], self.rectgameobject_weightRight.width, self.rectgameobject_weightRight.height )
		# tempUpRect = pygame.Rect( self.rectgameobject_heightUp.left - posUpdate[0], self.rectgameobject_heightUp.top - posUpdate[1], self.rectgameobject_heightUp.width, self.rectgameobject_heightUp.height )
		# tempDownRect = pygame.Rect( self.rectgameobject_heightDown.left - posUpdate[0], self.rectgameobject_heightDown.top - posUpdate[1], self.rectgameobject_heightDown.width, self.rectgameobject_heightDown.height )

		# pygame.draw.rect(surface,
		#  				pygame.Color('white'),
		#  				tempLeftRect,1)
		# pygame.draw.rect(surface,
		#  				pygame.Color('white'),
		#  				tempRightRect,1)
		# pygame.draw.rect(surface,
		#  				pygame.Color('white'),
		#  				tempUpRect,1)
		# pygame.draw.rect(surface,
		# 				pygame.Color('white'),
		# 				tempDownRect,1)

		tempRect = pygame.Rect(self.rectgameobject.left - posUpdate[0], self.rectgameobject.top - posUpdate[1], self.rectgameobject.width, self.rectgameobject.height)
		pygame.draw.rect(surface,
						pygame.Color('orange'),
						tempRect,5)

class Thorn(object):
	def __init__(self, pos):
		(self.x, self.y) = pos
		self.thorn_Weight = 20
		self.thorn_Height = 30
		self.tempTriangle = ([self.x, self.y], 
						[self.x+self.thorn_Weight, self.y], 
						[self.x+self.thorn_Weight/2, self.y-self.thorn_Height])

	def update(self):
		pass

	def render(self, surface, posUpdate):
		self.tempTriangle = ([self.x - posUpdate[0], self.y - posUpdate[1]], 
						[self.x+self.thorn_Weight - posUpdate[0], self.y - posUpdate[1]], 
						[self.x+self.thorn_Weight/2 - posUpdate[0], self.y-self.thorn_Height - posUpdate[1]])
		pygame.draw.polygon(surface, pygame.Color('white'), self.tempTriangle, 3)