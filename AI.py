# By Pytel

import random
import copy


import Chess
DEBUG = True


class Player:
	def __init__(self, color):
		self.color = color
		self.score = 0
		self.bord = None
		self.new_bord = None
		self.check_bord = None
		# herni stavy
		self.check = False
		self.garde = False
		self.mate = False
		# tah
		self.moves = None
		
	def Score(self):
		return self.score
		
	def MoveFromTo(self, bord, move_from, move_to):
		y_f = move_from[0]
		x_f = move_from[1]
		y_t = move_to[0]
		x_t = move_to[1]
		bord = self.new_bord.chessbord
		bord[y_t][x_t] = bord[y_f][x_f]
		bord[y_f][x_f] = None
	
	def PlaceCheckSum(self, position):
		figurs = self.new_bord.CheckPiece(position, self.color)
		cost_sum = 0
		for figur in figurs:
			y = figur[0]
			x = figur[1]
			cost_sum = cost_sum - self.new_bord.chessbord[y][x].cost
		return cost_sum
		
	"""
	Vygeneruje sachovnici nepratelskymi figurami
	"""
	def MakeCheckBord(self):
		self.check_bord = []
		for y in range(8):
			row = []
			for x in range(8):
				row.append( self.PlaceCheckSum([y,x]) )
			self.check_bord.append(row)
	
	def Attacked(self, chessman, destination):
		check = []
		check = self.new_bord.CheckPieceByType(destination, self.color, chessman.name, check)
		cost = 0
		# TODO
		for position in check:
			cest = cost + self.new_bord.chessbord[position[0]][position[1]].cost/2
		return cost
	
	def PlayCost(self, location, destination):
		y_l = location[0]
		x_l = location[1]
		y_d = destination[0]
		x_d = destination[1]
		chessman = self.new_bord.chessbord[y_l][x_l]
		cost = 0
		
		# uhyb
		if self.check_bord[y_l][x_l] != 0:
			cost = cost + self.bord.chessbord[y_l][x_l].cost
		
		# napadeni
		cost = cost + self.Attacked(chessman, destination)
		
		# sebrani figury
		if self.bord.chessbord[y_d][x_d] != None:
			cost = self.bord.chessbord[y_d][x_d].cost
			if self.check_bord[y_d][x_d] != 0:
				cost = cost - self.bord.chessbord[y_l][x_l].cost
		return cost
		
	""" 
	Hlavni funkce volana hrou
	Vraci zahrany tah
	"""
	def Move(self, bord):
		self.bord = bord
		self.new_bord = copy.deepcopy(bord)
		self.MakeCheckBord()
		self.moves = []
		pieces = self.MyPieces()
		for piece in pieces:
			print(piece)
			destinations = self.Moves(piece)
			for destination in destinations:
				# obodovani daneho tahu
				cost = self.PlayCost(piece, destination)
				self.moves.append([piece,destination,cost])
			
		# selekce tahu
		# tah nesmi koncit v sachu
		idx = 0
		while idx < len(self.moves):
			# teoreticke zahrani tahu
			safe_place = self.new_bord.chessbord[self.moves[idx][1][0]][self.moves[idx][1][1]]	# save target
			self.MoveFromTo(self.new_bord, self.moves[idx][0], self.moves[idx][1])
			if DEBUG and 0:
				print(" Theoretical", end='')
				self.new_bord.PrintBord()
				bord = self.new_bord.chessbord
				y = self.moves[idx][1][0]
				x = self.moves[idx][1][1]
				name = bord[y][x].name
				print(" Move", name,"from:", self.moves[idx][0], "to:", self.moves[idx][1])
			
			# najdi krale
			position = []
			position = self.new_bord.FindPiece(self.color, "king")
			if DEBUG and 0:
				print("Position of King:", position[0])
			#check = self.new_bord.CheckPiece(position[0], self.color)
			check = self.new_bord.IsPieceInCheck(position[0], self.color)
			
			# vraceni figurek do puvodniho stavu
			self.MoveFromTo(self.new_bord, self.moves[idx][1], self.moves[idx][0])
			self.new_bord.chessbord[self.moves[idx][1][0]][self.moves[idx][1][1]] = safe_place	# restore target
			
			# vyhodnoceni
			if check == True:
				print("del:", self.moves[idx])
				del self.moves[idx]
			else:
				idx = idx +1
			
		if len(self.moves) != 0:
			# setrideni podle treti polozky (cost)
			self.moves.sort(key=lambda x: x[2])
			if self.moves[-1][2] == 0:
				move = random.choice(self.moves)
			else:
				move = self.moves[-1]
			print(move)
		else:
			move = None
			
		if DEBUG:
			print(self.moves)
		
		return move
	
	def MyPieces(self):
		pieces = []
		bord = self.bord.chessbord
		for y in range(len(bord)):
			for x in range(len(bord[y])):
				if bord[y][x] != None:
					chessman = bord[y][x]
					if chessman.color == self.color:
						pieces.append([y,x])
		return pieces
		
	"""
	Vrati vsechny fyzicky mozne tahy pro fuguru na dane pozici
	"""
	def Moves(self, position):
		y = position[0];
		x = position[1];
		bord = self.bord.chessbord
		moves = []
		if bord[y][x] == None:
			return []
		chessman = bord[y][x]
		# postavy s nestandartnim pohybem
		if chessman.name == "pawn":
			moves = chessman.ChessmanMove(position, bord)
			
		# TODO
		#if chessman.name == "king":
			
		else:
			# pro vsechny vektory
			for vector in chessman.vector:
				y_v = y+vector[0]
				x_v = x+vector[1]
				while ((y_v <= 7 and y_v >= 0) and (x_v <= 7 and x_v >= 0)):
					if bord[y_v][x_v] == None:
						moves.append([y_v,x_v])
					elif bord[y_v][x_v].color != self.color:
						moves.append([y_v,x_v])
						break
					elif bord[y_v][x_v].color == self.color:
						break
					# aktualizace
					y_v = y_v+vector[0]
					x_v = x_v+vector[1]
			
			# pro veskery incrementalni pohyb
			for increment in chessman.incremental:
				y_n = y+increment[0];
				x_n = x+increment[1];
				if ((y_n <= 7 and y_n >= 0) and (x_n <= 7 and x_n >= 0)):
					if bord[y_n][x_n] == None or bord[y_n][x_n].color != self.color:
						moves.append([y_n,x_n])
				
		return moves
		
	
	def Print(self):
		print("Color:", self.color)
		print("Score:", self.score, "	Check:", self.check, "	Garde:", self.garde)
	
"""

"""