# By Pytel

DEBUG = True

class Chessman:
	def __init__(self, name = None, color = None):
		self.name = []	#pawn, rook, knight, bishop, queen, king
		self.color = color	# white, Black
		self.character = []
		self.cost = -1
		self.vector = []
		self.incremental = []
		self.moved = False
		if (name != None):
			self.SetPiece(name)
		
	def SetPawn(self):		# pesec
		self.name = "pawn"
		self.character = ['\u2659','\u265F']
		self.cost = 1		#Y,X
		self.incremental = [[1,0],[2,0],[-1,0],[-2,0]]
		if self.color == "white":
			del self.incremental[0]
			del self.incremental[0]
		elif self.color == "black":
			self.incremental.pop()
			self.incremental.pop()
		
	def SetRook(self):		# vez
		self.name = "rook"
		self.cost = 5
		self.character = ['\u2656','\u265C']
		self.vector = [[1,0],[-1,0],[0,1],[0,-1]]
		
	def SetKnight(self):	# kun
		self.name = "knight"
		self.cost = 3
		self.character = ['\u2658','\u265E']
		self.incremental = [[2,1],[2,-1],[1,2],[-1,2],[-2,1],[-2,-1],[1,-2],[-1,-2]]
		
	def SetBishop(self):	# strelec
		self.name = "bishop"
		self.cost = 3
		self.character = ['\u2657','\u265D']
		self.vector = [[1,1],[-1,1],[-1,-1],[1,-1]]
		
	def SetQueen(self):		# dama
		self.name = "queen"
		self.cost = 9
		self.character = ['\u2655','\u265B']
		self.vector = [[1,1],[-1,1],[-1,-1],[1,-1],[1,0],[-1,0],[0,1],[0,-1]]
		
	def SetKing(self):		# kral
		self.name = "king"
		self.character = ['\u2654','\u265A']
		self.incremental = [[1,1],[-1,1],[-1,-1],[1,-1],[1,0],[-1,0],[0,1],[0,-1]]
		
	def SetPiece(self, name):
		if (name == "pawn"):
			self.SetPawn()
		elif (name == "rook"):
			self.SetRook()
		elif (name == "knight"):
			self.SetKnight()
		elif (name == "bishop"):
			self.SetBishop()
		elif (name == "queen"):
			self.SetQueen()
		elif (name == "king"):
			self.SetKing()
	
	def Print(self):
		print(" ---Chessman--- ")
		if self.color == None:
			print(self.character[0], self.character[1], end='')
		elif self.color == "white":
			print(self.color, self.character[1], end='')
		elif self.color == "black":
			print(self.color, self.character[0], end='')
		print(" ", self.name, "cost:", self.cost)
		if len(self.vector) > 0:
			print("Move in vectros:", self.vector)
		else:
			print("Move incremental:", self.incremental)
		


class Game:
	def __init__(self):
		self.bord = Game.MakeBord(self)
		self.chessmans = []
		# hraci
		self.player_white = None
		self.player_black = None
		# vytvori set definovanych figur
		self.MakePieceSet()
		
	def SetPlayer(self, player, color):
		if color == "white":
			self.player_white = player
		elif color == "black":
			self.player_black = player
		
	def MakeBord(self):
		bord = []
		for y in range(8):
			row = []
			for x in range(8):
				#field = []
				row.append(None)
			bord.append(row)
		return bord
		
	def MakePieceSet(self):
		#pawn, rook, knight, bishop, queen, king
		self.chessmans.append(Chessman("pawn"))
		self.chessmans.append(Chessman("knight"))
		self.chessmans.append(Chessman("bishop"))
		self.chessmans.append(Chessman("rook"))
		self.chessmans.append(Chessman("queen"))
		self.chessmans.append(Chessman("king"))
		
	def MyPieces(self):
		
		return pieces
		
	def NewGame(self):
		# zahodi zbyle figurky
		for row in self.bord:
			for col in row:
				while col != None:
					col.pop()
		# vysazi zde nove figurky
		
		# cerny
		self.bord[0][0] = Chessman("rook", "black")
		self.bord[0][1] = Chessman("knight", "black")
		self.bord[0][2] = Chessman("bishop", "black")
		self.bord[0][3] = Chessman("queen", "black")
		self.bord[0][4] = Chessman("king", "black")
		self.bord[0][5] = Chessman("bishop", "black")
		self.bord[0][6] = Chessman("knight", "black")
		self.bord[0][7] = Chessman("rook", "black")
		# rada pescu
		for x in range(8):
			self.bord[1][x] = Chessman("pawn", "black")
			
		# bili
		# rada pescu
		for x in range(8):
			self.bord[6][x] = Chessman("pawn", "white")
		self.bord[7][0] = Chessman("rook", "white")
		self.bord[7][1] = Chessman("knight", "white")
		self.bord[7][2] = Chessman("bishop", "white")
		self.bord[7][3] = Chessman("queen", "white")
		self.bord[7][4] = Chessman("king", "white")
		self.bord[7][5] = Chessman("bishop", "white")
		self.bord[7][6] = Chessman("knight", "white")
		self.bord[7][7] = Chessman("rook", "white")
		
	def EvaluateMove(self, player_color, move_from, move_to):
		y_f = move_from[0]
		x_f = move_from[1]
		# move from test
		# invalid interval
		if (x_f > 7 or x_f < 0 or x_f > 7 or x_f < 0):
			if DEBUG:
				print("Invalid from coordinates! cord:", move_from)
			return False
		# from empty place
		if self.bord[y_f][x_f] == None:
			if DEBUG:
				print("Invalid from coordinates!")
			return False
		# invalid color
		if self.bord[y_f][x_f].color != player_color:
			if DEBUG:
				print("Invalid player color!")
			return False
		
		# move to test
		y_t = move_to[0]
		x_t = move_to[1]
		# invalid destination coordinates
		if (x_t > 7 or x_t < 0 or x_t > 7 or x_t < 0):
			if DEBUG:
				print("Invalid destination coordinates!")
			return False
		# invalid destination color 
		if self.bord[y_t][x_t] != None and self.bord[y_t][x_t].color == player_color:
			if DEBUG:
				print("Invalid destination color!")
			return False
		
		
		# physicali valid move
		chessman = self.bord[y_f][x_f]
		chessman.Print()
		
		valid = False
		# pro vsechny vektory
		for vector in chessman.vector:
			y_v = y_f
			x_v = x_f
			while (y_v < 7 or y_v > 0 or x_v < 7 or x_v > 0):
				y_v = y_v+vector[0]
				x_v = x_v+vector[1]
				if y_v == y_t and x_v == x_t:
					valid = True
					break
			if valid == True:
				break
		
		# pro veskery incrementalni pohyb
		for increment in chessman.incremental:
			if y_f+increment[0] == y_t and x_f+increment[1] == x_t:
				valid = True
				break
		
		# game_logicaly valid move
		if valid == False:
			return False
		elif valid == True:
			self.bord[y_f][x_f] = None
		
		# zvlastni tahy:
		 # pesec
		if chessman.moved == False and chessman.name == "pawn":
			chessman.incremental.pop()
		 # kral
		
		# jiz se s figurou hybalo
		chessman.moved = True
		
		# jde na prazdne pole
		if self.bord[y_t][x_t] == None:
			self.bord[y_t][x_t] = chessman
	
	def Playing(self):
		return (not(self.player_white.mate) and not(self.player_black.mate))
		
	def PrintBord(self):
		print(" ---Bord--- ")
		for y in range(len(self.bord)):
			# indexovani radku
			row = 8-y
			print(row, end='')
			print("|", end='')
			# jednotlive radky
			for x in range(len(self.bord[y])):
				if self.bord[y][x] != None:
					if (self.bord[y][x].color == "white"):
						print(self.bord[y][x].character[1], end='')
					else:
						print(self.bord[y][x].character[0], end='')
				else:
					print("_", end='')
			print("|")
		# pismenka
		print("  ", end='')
		for x in range(8):
			char = 65 + x
			print(chr(char), end='')
		print()
			
	def PrintChessmans(self):
		for chessman in self.chessmans:
			chessman.Print()
		
	

"""

"""