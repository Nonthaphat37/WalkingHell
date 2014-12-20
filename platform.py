import pygame
from pygame.locals import *

class Platform(object):
	def __init__(self, pos, weight, height, color, thick = 5):
		(self.x, self.y) = pos
		self.platform_Weight = weight
		self.platform_Height = height
		self.rectfloor = pygame.Rect(self.x, self.y, self.platform_Weight, self.platform_Height)
		self.color = color
		self.thick = thick
		self.vx = 0

	def init(self):
		pass

	def update(self):
		pass

	def render(self, surface, camPos):
		tempRect = pygame.Rect(self.rectfloor.left - camPos[0], self.rectfloor.top - camPos[1], self.rectfloor.width, self.rectfloor.height)
		pygame.draw.rect(surface,
						self.color,
						tempRect,self.thick)

class Floor(Platform):
	def __init__(self, pos, weight, height, color, thick = 5):
		super(Floor, self).__init__(pos, weight, height, color, thick)

	def update(self):
		pass

	def render(self, surface, camPos):
		super(Floor, self).render(surface, camPos)

class FloorSlide(Platform):
	def __init__(self, pos, weight, height, color, range_x1, range_x2):
		super(FloorSlide, self).__init__(pos, weight, height, color)
		self.range_x1 = range_x1
		self.range_x2 = range_x2
		self.vx = 2

	def update(self):
		if self.x <= self.range_x1:
			self.vx = 2
		elif self.x >= self.range_x2-self.platform_Weight:
			self.vx = -2
		self.x += self.vx
		self.rectfloor = pygame.Rect(self.x, self.y, self.platform_Weight, self.platform_Height)

	def render(self, surface, camPos):
		super(FloorSlide, self).render(surface, camPos)

class Door(Platform):
	def __init__(self, pos, weight, height, color, thick, correctCode):
		super(Door, self).__init__(pos, weight, height, color, thick)
		self.x_Start = self.x
		self.y_Start = self.y
		self.correctCode = correctCode
		self.is_correctCode = False
		self.code = []
		self.fontType = None
		self.fontSize = 40
		self.font = pygame.font.SysFont(self.fontType,self.fontSize)
		self.checkCollision = False
		self.iphone_rect = pygame.Rect(self.x_Start, self.y_Start, 70, 143)

		self.iphone = pygame.image.load('objectPicture/iphone.png')


	def update(self, code):
		self.code = code
		if self.checkCollision:
			if self.code == self.correctCode:
				self.is_correctCode = True
		if self.is_correctCode:
			self.y -= 1
			self.rectfloor = pygame.Rect(self.x, self.y, self.platform_Weight, self.platform_Height)
		else:
			self.y = self.y_Start
			self.rectfloor = pygame.Rect(self.x, self.y, self.platform_Weight, self.platform_Height)
		self.iphone_rect = pygame.Rect(self.x_Start  - 250, self.y_Start + self.platform_Height -143, 70, 143)


	def render(self, surface, camPos):
		super(Door, self).render(surface, camPos)
		color = (150,255,200)
		self.text_Code1 = self.font.render('PizzaCompany', True, color)
		surface.blit(self.text_Code1,(self.x_Start - camPos[0]-320, self.y_Start - camPos[1] + 720))
		color = (200,200,0)
		if self.is_correctCode:
			self.text = self.font.render('[' + (' '.join(str(Ccode) for Ccode in self.correctCode) + ']'), True, color)
			surface.blit(self.text,(self.x_Start - camPos[0]-20, self.y_Start - camPos[1] + 720))
		else:
			self.text = self.font.render('[' + (' '.join(str(code) for code in self.code) + ']'), True, color)
			surface.blit(self.text, (self.x_Start - camPos[0]-20, self.y_Start - camPos[1] + 720))
		surface.blit(self.iphone, (self.x_Start - camPos[0] - 250, self.y_Start + self.platform_Height - camPos[1] -143))

	def checkCollisionToCode(self, checkCollision):
		self.checkCollision = checkCollision