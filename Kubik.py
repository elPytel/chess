# By Pytel

import random

DEBUG = True


class Player:
	def __init__(self, color):
		self.color = color
		self.score = 0
		self.bord = None
		# herni stavy
		self.check = False
		self.garde = False
		self.mate = False
		# tah
		self.moves = None
		
	def Score(self):
		return self.score
		
	def Move(self, bord):
		self.bord = bord
		self.moves = []
		pieces = self.MyPieces()
		for piece in pieces:
			print(piece)
			destinations = self.Moves(piece)
			for destination in destinations:
				self.moves.append([piece,destination])
		"""
		move_from = [6,3]
		move_to = [4,3]
		move = [move_from, move_to]
		"""
		move = random.choice(self.moves)
		print(move)
		return move
	
		
	def MyPieces(self):
		pieces = []
		for y in range(len(self.bord)):
			for x in range(len(self.bord[y])):
				if self.bord[y][x] != None:
					chessman = self.bord[y][x]
					if chessman.color == self.color:
						pieces.append([y,x])
		return pieces
		
		
	def Moves(self, position):
		y = position[0];
		x = position[1];
		if self.bord[y][x] == None:
			return []
		chessman = self.bord[y][x]
		# TODO
		#if chessman.name == "pawn":
			
		#if chessman.name == "king":
			
		moves = []
		# pro vsechny vektory
		for vector in chessman.vector:
			y_v = y+vector[0]
			x_v = x+vector[1]
			while ((y_v <= 7 and y_v >= 0) and (x_v <= 7 and x_v >= 0)):
				if self.bord[y_v][x_v] == None:
					moves.append([y_v,x_v])
				elif self.bord[y_v][x_v].color != self.color:
					moves.append([y_v,x_v])
					break
				elif self.bord[y_v][x_v].color == self.color:
					break
				# aktualizace
				y_v = y_v+vector[0]
				x_v = x_v+vector[1]
		
		# pro veskery incrementalni pohyb
		for increment in chessman.incremental:
			y_n = y+increment[0];
			x_n = x+increment[1];
			if ((y_n <= 7 and y_n >= 0) and (x_n <= 7 and x_n >= 0)):
				if self.bord[y_n][x_n] == None or self.bord[y_n][x_n].color != self.color:
					moves.append([y_n,x_n])
			
		return moves
		
	
	def Print(self):
		print("Color:", self.color)
		print("Score:", self.score)
	
"""

"""