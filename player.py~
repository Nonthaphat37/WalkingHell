import pygame
from pygame.locals import *
import pyganim

class Player(object):
	velocity_X = 5
	velocity_Y = 16
	G = -1

	def __init__(self, pos, speed=(0, 0)):
		self.sprite_player_StandLeft = pyganim.PygAnimation([('objectPicture\playerStand_left.png', 0.1)])
		self.sprite_player_StandRight = pyganim.PygAnimation([('objectPicture\playerStand_right.png', 0.1)])
		self.sprite_player_MoveLeft = pyganim.PygAnimation([('objectPicture\playerMove_left1.png', 0.1),
										('objectPicture\playerMove_left2.png', 0.1),
										('objectPicture\playerMove_left3.png', 0.1),
										('objectPicture\playerMove_left4.png', 0.1)])
		self.sprite_player_MoveRight = pyganim.PygAnimation([('objectPicture\playerMove_right1.png', 0.1),
										('objectPicture\playerMove_right2.png', 0.1),
										('objectPicture\playerMove_right3.png', 0.1),
										('objectPicture\playerMove_right4.png', 0.1)])
		self.sprite_player_JumpLeft = pyganim.PygAnimation([('objectPicture\playerJump_left.png', 0.1)])
		self.sprite_player_JumpRight = pyganim.PygAnimation([('objectPicture\playerJump_right.png', 0.1)])
		self.animation_Player = [self.sprite_player_StandLeft, self.sprite_player_StandRight, 
								self.sprite_player_MoveLeft, self.sprite_player_MoveRight,
								self.sprite_player_JumpLeft, self.sprite_player_JumpRight]
		self.state_Player = 'standright'


		self.player_Weight = 100
		self.player_Height = 117

		(self.x, self.y) = pos
		(self.vx, self.vy) = speed
		self.ovx = Player.velocity_X-2
		self.vx_onPlatform = 0

		self.rect_ErrorSize = 1
		self.rect_ErrorPosition_Y = 25
		self.rect_ErrorPosition_X = 10
		self.rect_Weight = self.player_Weight-self.rect_ErrorPosition_Y*2
		self.rect_Height = self.player_Height-self.rect_ErrorPosition_X*2
		self.pos_rectUpdate()
		
		self.colLeft = False
		self.colRight = False
		self.colUp = False
		self.colDown = False
		self.colAction = False
		self.rectplayer = pygame.Rect(self.x, self.y, self.player_Weight, self.player_Height)


		self.y -= self.player_Height


	def init(self):
		pass

	def is_Floor(self, floor):
		self.is_floor = floor

	def update(self):
		self.x = self.x + self.vx + self.vx_onPlatform
		self.updateGravity()
		self.pos_rectUpdate()

	def updateGravity(self):
		self.y -= self.vy
		self.vy += Player.G

	def move_left(self):
		self.state_Player = 'moveleft'
		if not self.colAction:
			self.vx = -Player.velocity_X
		else:
			self.vx = -self.ovx

	def move_right(self):
		self.state_Player = 'moveright'
		if not self.colAction:
			self.vx = Player.velocity_X
		else:
			self.vx = self.ovx

	def move_stand(self):
		if self.state_Player == 'moveleft' or self.state_Player == 'jumpleft':
			self.state_Player = 'standleft'
		elif self.state_Player == 'moveright' or self.state_Player == 'jumpright':
			self.state_Player = 'standright'
		self.vx = 0

	def move_jump(self):
		self.vy = Player.velocity_Y
		self.y -= self.vy

	def render(self, surface, posUpdate):
		pos = (int(self.x - posUpdate[0]),int(self.y - posUpdate[1]))

		#-------------------- Player Animation ----------------------#
		if self.state_Player == 'standleft':
			self.animation_Player[0].play()
			self.animation_Player[0].blit(surface, pos)
		elif self.state_Player == 'standright':
			self.animation_Player[1].play()
			self.animation_Player[1].blit(surface, pos)
		elif self.state_Player == 'moveleft':
			self.animation_Player[2].play()
			self.animation_Player[2].blit(surface, pos)
		elif self.state_Player == 'moveright':
			self.animation_Player[3].play()
			self.animation_Player[3].blit(surface, pos)
		elif self.state_Player == 'jumpleft':
			self.animation_Player[4].play()
			self.animation_Player[4].blit(surface, pos)
		elif self.state_Player == 'jumpright':
			self.animation_Player[5].play()
			self.animation_Player[5].blit(surface, pos)

		#------------------------ Player Colliders------------------#
		tempLeftRect = pygame.Rect( self.rectplayer_weightLeft.left - posUpdate[0], self.rectplayer_weightLeft.top - posUpdate[1], self.rectplayer_weightLeft.width, self.rectplayer_weightLeft.height )
		tempRightRect = pygame.Rect( self.rectplayer_weightRight.left - posUpdate[0], self.rectplayer_weightRight.top - posUpdate[1], self.rectplayer_weightRight.width, self.rectplayer_weightRight.height )
		tempUpRect = pygame.Rect( self.rectplayer_heightUp.left - posUpdate[0], self.rectplayer_heightUp.top - posUpdate[1], self.rectplayer_heightUp.width, self.rectplayer_heightUp.height )
		tempDownRect = pygame.Rect( self.rectplayer_heightDown.left - posUpdate[0], self.rectplayer_heightDown.top - posUpdate[1], self.rectplayer_heightDown.width, self.rectplayer_heightDown.height )

			#pygame.draw.rect(surface,
			# 				pygame.Color('white'),
			# 				tempLeftRect,1)
			#pygame.draw.rect(surface,
			# 				pygame.Color('white'),
			# 				tempRightRect,1)
			#pygame.draw.rect(surface,
			# 				pygame.Color('white'),
			# 				tempUpRect,1)
			#pygame.draw.rect(surface,
			#				pygame.Color('white'),
			#				tempDownRect,1)


	def pos_rectUpdate(self):
		self.rectplayer_weightLeft = pygame.Rect(self.x, 
												self.y+self.rect_ErrorPosition_X, 
												self.rect_ErrorSize, 
												self.rect_Height)
		self.rectplayer_weightRight = pygame.Rect(self.x+self.player_Weight, 
												self.y+self.rect_ErrorPosition_X,
												self.rect_ErrorSize, 
												self.rect_Height)
		self.rectplayer_heightUp = pygame.Rect(self.x+self.rect_ErrorPosition_Y, 
												self.y,
												self.rect_Weight, 
												self.rect_ErrorSize)
		self.rectplayer_heightDown = pygame.Rect(self.x+self.rect_ErrorPosition_Y, 
												self.y+self.player_Height-self.rect_ErrorSize, 
												self.rect_Weight, 
												self.rect_ErrorSize)
		self.rectplayer = pygame.Rect(self.x, self.y, self.player_Weight, self.player_Height)
