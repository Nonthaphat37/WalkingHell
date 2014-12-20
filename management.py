import pygame
from pygame.locals import *
from gamelib import SimpleGame 

class Controller():

	def __init__(self):
		pygame.init()

	def is_key_pressed(self, key):
		keys_pressed = pygame.key.get_pressed()
		if key < 0 or key >= len(keys_pressed):
			return False
		return (keys_pressed[key])

	def controllerPlayer(self, player):
		if self.is_key_pressed(K_a) or self.is_key_pressed(K_LEFT):
			player.move_left()
		elif self.is_key_pressed(K_d) or self.is_key_pressed(K_RIGHT):
			player.move_right()
		elif player.colDown:
			player.move_stand()
		if self.is_key_pressed(K_SPACE) and player.colDown:
			player.move_jump()
		if self.is_key_pressed(K_j) and (player.colLeft or player.colRight):
			player.colAction = True
		else:
			player.colAction = False


	def collisionEngine(self, player, platform, gameobject, thorn):
		player.colDown = False
		player.colUp = False
		player.colLeft = False
		player.colRight = False

		for i in range(len(gameobject)):
			gameobject[i].colDown = False
			gameobject[i].colUp = False
			gameobject[i].colLeft = False
			gameobject[i].colRight = False
		for currentPlat in platform:
			self.collisionPlayerinPlatform(player, currentPlat)
			self.collisionGameObjectinPlatform(gameobject, currentPlat)
		self.collisionGameObjectinGameObject(player, gameobject)
		self.collisionPlayerinGameObject(player, gameobject)
		
		for i in range(len(gameobject)):
			if not gameobject[i].colDown:
				if gameobject[i].vx > 0:
					gameobject[i].vx = player.velocity_X
				elif gameobject[i].vx < 0:
					gameobject[i].vx = -player.velocity_X

		return self.collisionPlayerinThorn(player, thorn)


	def collisionPlayerinPlatform(self, player, currentPlat):
		if player.rectplayer_heightDown.colliderect(currentPlat.rectfloor):
			player.colDown = True
			player.y = currentPlat.y-player.player_Height+player.rect_ErrorSize
			player.vy = 0
			player.vx_onPlatform = currentPlat.vx
		elif player.rectplayer_heightUp.colliderect(currentPlat.rectfloor):
			player.colUp = True
			player.y = currentPlat.y+currentPlat.platform_Height-player.rect_ErrorSize
		elif player.rectplayer_weightLeft.colliderect(currentPlat.rectfloor):
			player.colLeft = True
			player.x = currentPlat.x+currentPlat.platform_Weight-player.rect_ErrorSize
			player.vx = 0
		elif player.rectplayer_weightRight.colliderect(currentPlat.rectfloor):
			player.colRight = True
			player.x = currentPlat.x-player.player_Weight+player.rect_ErrorSize
			player.vx = 0

	def collisionGameObjectinPlatform(self, gameobject, currentPlat):
		for i in range(len(gameobject)):
			if gameobject[i].rectgameobject_heightDown.colliderect(currentPlat.rectfloor):
				gameobject[i].colDown = True
				gameobject[i].y = currentPlat.y-gameobject[i].gameobject_Height+gameobject[i].rect_ErrorSize
				gameobject[i].vy = 0
				gameobject[i].vx = 0
				gameobject[i].vx_onPlatform = currentPlat.vx
			elif gameobject[i].rectgameobject_heightUp.colliderect(currentPlat.rectfloor):
				gameobject[i].colUp = True
				gameobject[i].y = currentPlat.y+currentPlat.platform_Height-gameobject[i].rect_ErrorSize
				gameobject[i].vy = 0
			elif gameobject[i].rectgameobject_weightLeft.colliderect(currentPlat.rectfloor):
				gameobject[i].colLeft = True
				gameobject[i].x = currentPlat.x+currentPlat.platform_Weight-gameobject[i].rect_ErrorSize
				gameobject[i].vx = 0
			elif gameobject[i].rectgameobject_weightRight.colliderect(currentPlat.rectfloor):
				gameobject[i].colRight = True
				gameobject[i].x = currentPlat.x-gameobject[i].gameobject_Weight+gameobject[i].rect_ErrorSize
				gameobject[i].vx = 0

	def collisionPlayerinGameObject(self, player, gameobject):
		for i in range(len(gameobject)):
			if player.rectplayer_heightDown.colliderect(gameobject[i].rectgameobject):
				player.colDown = True
				player.y = gameobject[i].y-player.player_Height+player.rect_ErrorSize
				player.vy = 0
				player.vx_onPlatform = gameobject[i].vx_onPlatform
			elif player.rectplayer_weightLeft.colliderect(gameobject[i].rectgameobject):
				player.colLeft = True
				if player.colAction and not gameobject[i].colLeft:
					gameobject[i].vx = player.vx - player.vx_onPlatform + -abs(gameobject[i].vx_onPlatform)
				else:
					player.x = gameobject[i].x+gameobject[i].gameobject_Weight+player.rect_ErrorSize
					player.vx = 0
					gameobject[i].vx = 0
			elif player.rectplayer_weightRight.colliderect(gameobject[i].rectgameobject):
				player.colRight = True
				if player.colAction and not gameobject[i].colRight:
					gameobject[i].vx = player.vx + player.vx_onPlatform + abs(gameobject[i].vx_onPlatform)
				else:
					player.x = gameobject[i].x-player.player_Weight+player.rect_ErrorSize
					player.vx = 0
					gameobject[i].vx = 0
			else:
				if gameobject[i].vx != player.velocity_X and gameobject[i].vx != -player.velocity_X:
					gameobject[i].vx = 0

	def collisionGameObjectinGameObject(self, player, gameobject):
		for i in range(len(gameobject)):
			for j in range(len(gameobject)):
				if i != j:
					if gameobject[i].rectgameobject_heightDown.colliderect(gameobject[j].rectgameobject):
						gameobject[i].colDown = True
						gameobject[i].y = gameobject[j].y-gameobject[i].gameobject_Height+gameobject[i].rect_ErrorSize
						gameobject[i].vy = 0
						gameobject[i].vx = 0
					elif gameobject[i].rectgameobject_weightLeft.colliderect(gameobject[j].rectgameobject):
						gameobject[i].colLeft = True
						gameobject[i].x = gameobject[j].x+gameobject[j].gameobject_Weight-gameobject[i].rect_ErrorSize
						gameobject[i].vx = 0
						if player.rectplayer_weightLeft.colliderect(gameobject[i].rectgameobject):
							player.vx = 0
							player.x = gameobject[i].x+gameobject[i].gameobject_Weight-player.rect_ErrorSize
						elif player.rectplayer_weightRight.colliderect(gameobject[i].rectgameobject):
							player.vx = 0
							player.x = gameobject[i].x-player.player_Weight+player.rect_ErrorSize
					elif gameobject[i].rectgameobject_weightRight.colliderect(gameobject[j].rectgameobject):
						gameobject[i].colRight = True
						gameobject[i].x = gameobject[j].x-gameobject[i].gameobject_Weight+gameobject[i].rect_ErrorSize
						gameobject[i].vx = 0
						if player.rectplayer_weightLeft.colliderect(gameobject[i].rectgameobject):
							player.vx = 0
							player.x = gameobject[i].x+gameobject[i].gameobject_Weight-player.rect_ErrorSize
						elif player.rectplayer_weightRight.colliderect(gameobject[i].rectgameobject):
							player.vx = 0
							player.x = gameobject[i].x-player.player_Weight+player.rect_ErrorSize

	def collisionPlayerinIphone(self, player, iphone):
		return player.rectplayer.colliderect(iphone.iphone_rect)

	def collisionPlayerinThorn(self, player, thorn):
		for i in range(len(thorn)):
			if player.rectplayer.collidepoint(thorn[i].x, thorn[i].y):
				return True
		return False


	def updateStatePlayer(self, player):
		if not player.colDown:
			if player.state_Player == 'moveleft' or player.state_Player == 'standleft':
				player.state_Player = 'jumpleft'
			elif player.state_Player == 'moveright' or player.state_Player == 'standright':
				player.state_Player = 'jumpright'

class Camera():
	# position, offset
	# Camera.position = [0,0]
	def __init__(self, offset = [0,0]):
		self.offset = offset
		self.position = [0,0]

	def update(self, playerPosition = [0, 0]):
		self.position[0] = playerPosition[0] - self.offset[0]
		self.position[1] = playerPosition[1] - self.offset[1]