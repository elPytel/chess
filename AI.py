# By Pytel

import random

DEBUG = True


class Player:
	def __init__(self, color, game):
		self.color = color
		self.score = 0
		self.game = game
		# herni stavy
		self.check = False
		self.garde = False
		self.mate = False
		
	def Score(self):
		return self.score
		
	def Move(self):
		move_from = [6,3]
		move_to = [4,3]
		move = [move_from, move_to]
		return move
	
	def Print(self):
		print("Color:", self.color)
		print("Score:", self.score)
	
"""

"""