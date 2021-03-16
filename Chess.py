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
			
	def PawnMove(self, position, bord):
		moves = []
		y = position[0]
		x = position[1]
		# pohyb dopredu
		for increment in self.incremental:
			y_i = y+increment[0]
			x_i = x+increment[1]
			# je to validni pole?
			if (y_i > 7 or y_i < 0 or x_i > 7 or x_i < 0):
				continue
			# je to pole volne?
			if bord[y_i][x_i] == None:
				if DEBUG and 0:
					print("position y:", y_i,"x:", x_i," is free")
				moves.append([y_i,x_i])
			else:
				break
		
		# utok	
		for x_i in [-1,1]:
			x_i = x+x_i
			if self.color == "white":
				y_i = y-1
			if self.color == "black":
				y_i = y+1
			# je to validni pole?
			if (y_i > 7 or y_i < 0 or x_i > 7 or x_i < 0):
				continue
			# je to pole obsazene?
			if bord[y_i][x_i] != None and bord[y_i][x_i].color != self.color:
				moves.append([y_i,x_i])
			
		return moves
	
	# TODO
	def ChessmanMove(self, position, bord):
		moves = []
		if self.name == "pawn":
			moves = self.PawnMove(position, bord)
		#if self.name = "king":
		
		return moves
	
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
		
class Chessbord:
	def __init__(self):
		self.chessbord = self.MakeBord()
		self.white_bead = []
		self.black_bead = []
		
	def MakeBord(self):
		bord = []
		for y in range(8):
			row = []
			for x in range(8):
				#field = []
				row.append(None)
			bord.append(row)
		return bord
	
	def FindPiece(self, color, name):
		position = []
		for y in range(len(self.chessbord)):
			for x in range(len(self.chessbord[y])):
				if self.chessbord[y][x] != None:
					chessman = self.chessbord[y][x]
					if chessman.color == color and chessman.name == name:
						position.append([y,x])
		return position
		
	def CheckPieceByType(self, position, color, enemy_type):
		y = position[0]
		x = position[1]
		incremnets = []
		vectors = []
		
		if enemy_type == "king":
			incremnets = [[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
		elif enemy_type == "pawn":
			if color == "white":
				incremnets = [[-1, -1],[-1, 1]]
			elif color == "black":
				incremnets = [[1, -1],[1, 1]]
		else:
			incremnets = Chessman(enemy_type).incremental
			vectors = Chessman(enemy_type).vector
		#print(incremnets)
		
		# pro vektory
		for vector in vectors:
			y_v = y+vector[0]
			x_v = x+vector[1]
			while (y_v <= 7 and y_v >= 0 and x_v <= 7 and x_v >= 0):
				box = self.chessbord[y_v][x_v]
				if box != None:
					if box.color == color:
						break
					elif box.color != color and box.name != enemy_type:
						break
					elif box.name == enemy_type:
						if DEBUG:
							print("Position of enemy", enemy_type, ":", [y_v,x_v])
						return True
				# aktualizace
				y_v = y_v+vector[0]
				x_v = x_v+vector[1]
			
		# pro incrementalni pohyb
		for increment in incremnets:
			y_i = y + increment[0];
			x_i = x + increment[1];
			if (y_i > 7 or y_i < 0 or x_i > 7 or x_i < 0):
				continue
			box = self.chessbord[y_i][x_i]
			if box != None and box.color != color and box.name == enemy_type:
				if DEBUG:
					print("Position of enemy", enemy_type, ":", [y_i,x_i])
				return True
		
		return False
	
	def CheckPiece(self, position, color):	# kontrola napadeni
		#print(self.chessbord[position[0]][position[1]].name, "position:", position)
		# king check
		if self.CheckPieceByType(position, color, "pawn"):
			return True
		if self.CheckPieceByType(position, color, "rook"):
			return True
		if self.CheckPieceByType(position, color, "knight"):
			return True
		if self.CheckPieceByType(position, color, "bishop"):
			return True
		if self.CheckPieceByType(position, color, "queen"):
			return True
		if self.CheckPieceByType(position, color, "king"):
			return True
		
		return False
		
	def PrintBord(self):
		bord = self.chessbord
		print(" ---Bord--- ")
		print("  01234567 ")
		for y in range(len(bord)):
			# indexovani radku
			row = 8-y
			print(row, end='')
			print("|", end='')
			# jednotlive radky
			for x in range(len(bord[y])):
				if bord[y][x] != None:
					if (bord[y][x].color == "white"):
						print(bord[y][x].character[1], end='')
					else:
						print(bord[y][x].character[0], end='')
				else:
					print("_", end='')
			print("|", end='')
			print(y)
		# pismenka
		print("  ", end='')
		for x in range(8):
			char = 65 + x
			print(chr(char), end='')
		print()

class Game:
	def __init__(self):
		# sachovnice
		self.bord = Chessbord()
		# hraci
		self.player_white = None
		self.player_black = None
		
	def SetPlayer(self, player, color):
		if color == "white":
			self.player_white = player
		elif color == "black":
			self.player_black = player
		
	def NewGame(self):
		# zahodi zbyle figurky
		bord = self.bord.chessbord
		for row in bord:
			for col in row:
				while col != None:
					col.pop()
		# vysazi zde nove figurky
		
		# cerny
		bord[0][0] = Chessman("rook", "black")
		bord[0][1] = Chessman("knight", "black")
		bord[0][2] = Chessman("bishop", "black")
		bord[0][3] = Chessman("queen", "black")
		bord[0][4] = Chessman("king", "black")
		bord[0][5] = Chessman("bishop", "black")
		bord[0][6] = Chessman("knight", "black")
		bord[0][7] = Chessman("rook", "black")
		# rada pescu
		for x in range(8):
			bord[1][x] = Chessman("pawn", "black")
			
		# bili
		# rada pescu
		for x in range(8):
			bord[6][x] = Chessman("pawn", "white")
		bord[7][0] = Chessman("rook", "white")
		bord[7][1] = Chessman("knight", "white")
		bord[7][2] = Chessman("bishop", "white")
		bord[7][3] = Chessman("queen", "white")
		bord[7][4] = Chessman("king", "white")
		bord[7][5] = Chessman("bishop", "white")
		bord[7][6] = Chessman("knight", "white")
		bord[7][7] = Chessman("rook", "white")
	
	def EvaluateGarde(self, color):
		if color == "white":
			coordinates = self.bord.FindPiece("white", "queen")
			for position in coordinates:
				if self.bord.CheckPiece(position, "white"):
					print(color, "garde!")
					self.player_white.garde = True
				else:
					self.player_white.garde = False
		elif color == "black":
			coordinates = self.bord.FindPiece("black", "queen")
			for position in coordinates:
				if self.bord.CheckPiece(position, "black"):
					print(color, "garde!")
					self.player_black.garde = True
				else:
					self.player_black.garde = False
		
	def EvaluateCheck(self, color):
		if color == "white":
			old_check = self.player_white.check
			coordinates = self.bord.FindPiece("white", "king")
			if self.bord.CheckPiece(coordinates[0], "white"):
				print(color, "check!")
				self.player_white.check = True
			else:
				self.player_white.check = False
			
		if color == "black":
			coordinates = self.bord.FindPiece("black", "king")
			if self.bord.CheckPiece(coordinates[0], "black"):
				print(color, "check!")
				self.player_black.check = True
			else:
				self.player_black.check = False
		
	def EvaluateMove(self, player_color, move_from, move_to):
		y_f = move_from[0]
		x_f = move_from[1]
		bord = self.bord.chessbord
		# move from test
		# invalid interval
		if (y_f > 7 or y_f < 0 or x_f > 7 or x_f < 0):
			if DEBUG:
				print("Invalid from coordinates! cord:", move_from)
			return False
		# from empty place
		if bord[y_f][x_f] == None:
			if DEBUG:
				print("Invalid from coordinates!")
			return False
		# invalid color
		if bord[y_f][x_f].color != player_color:
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
		if bord[y_t][x_t] != None and bord[y_t][x_t].color == player_color:
			if DEBUG:
				print("Invalid destination color!")
			return False
		
		
		# physicali valid move
		chessman = bord[y_f][x_f]
		chessman.Print()
		
		valid = False
		if bord[y_f][x_f].name == "pawn":
			moves = []
			moves = bord[y_f][x_f].ChessmanMove(move_from, bord)
			if move_to in moves:
				valid = True
		else:
			# pro vsechny vektory
			for vector in chessman.vector:
				y_v = y_f+vector[0]
				x_v = x_f+vector[1]
				while (y_v <= 7 and y_v >= 0 and x_v <= 7 and x_v >= 0):
					if DEBUG and 0:
						print(y_v, x_v)
					if bord[y_v][x_v] != None:
						if bord[y_v][x_v].color == player_color:
							break
					if y_v == y_t and x_v == x_t:
						valid = True
						break
					# aktualizace
					y_v = y_v+vector[0]
					x_v = x_v+vector[1]
					
				if valid == True:
					break
			
			# pro veskery incrementalni pohyb
			for increment in chessman.incremental:
				if y_f+increment[0] == y_t and x_f+increment[1] == x_t:
					valid = True
					break
		
		# game_logicaly valid move
		if valid == False:
			if DEBUG:
				print("Can't get there!")
			return False
		elif valid == True:
			bord[y_f][x_f] = None
		
		# zvlastni tahy:
		 # pesec
		if chessman.moved == False and chessman.name == "pawn":
			chessman.incremental.pop()
		 # kral		
		 # test na validni tah hralem
		if chessman.name == "king" and self.bord.CheckPiece(move_to, player_color):
			print("Hara-kiri1")
			return False
		
		# jiz se s figurou hybalo
		chessman.moved = True
		
		# jde na prazdne pole
		if bord[y_t][x_t] == None:
			bord[y_t][x_t] = chessman
			return True
		# jde na obsazene pole
		elif bord[y_t][x_t].color != player_color:
			if DEBUG:
				print("Taken:", bord[y_t][x_t].color, bord[y_t][x_t].name)
			if player_color == "white":
				self.player_white.score = self.player_white.score + bord[y_t][x_t].cost
			elif player_color == "black":
				self.player_black.score = self.player_black.score + bord[y_t][x_t].cost
			# konec hry, smrt krale
			if bord[y_t][x_t].name == "king":
				if player_color == "white":
					self.player_black.mate = True
				elif player_color == "black":
					self.player_white.mate = True
				bord[y_f][x_f] = chessman
				return True
			
			# zahrani kamene
			bord[y_t][x_t] = chessman
			
		else:
			print("Ups, something Faigled...")
			return False
		
		# test na sach enemy krale & garde
		if player_color == "white":
			self.EvaluateCheck("black")
			self.EvaluateGarde("black")
		elif player_color == "black":
			self.EvaluateCheck("white")
			self.EvaluateGarde("white")
		
		#test na vlastni sach & garde
		old_check = False
		self.EvaluateCheck(player_color)
		self.EvaluateGarde(player_color)
		if player_color == "white":
			old_check = self.player_white.check
			if old_check and self.player_white.check:
				print("Hara-kiri2 - neuhnul")
				return False
		elif player_color == "black":
			if old_check and self.player_black.check:
				print("Hara-kiri2 - neuhnul")
				return False
		
		return True
	
	def Playing(self):
		return (not(self.player_white.mate) and not(self.player_black.mate))
		
	def Won(self, color):
		if color == "white":
			return not(self.player_white.mate)
		elif color == "black":
			return not(self.player_black.mate)
		return False
		
	def PrintBord(self):
		self.bord.PrintBord()
		

"""

"""