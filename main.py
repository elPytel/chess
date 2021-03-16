# By Pytel

import time

import Chess
import AI
import AI_random

"""
Sachy

# TODO
 - tahy s pinclem
 |- brani mimochodem
 - tahy s kralem
 |- rosada

 - vyhodnoceni None tahu
 |- je to pat
 |- hrac se vzdava

# DONE
 - Generator desky
 - validace tahu
 - ohrozeni
 |- figury napadajici danou pozici
 |- sach
 |- garde
 - sach-mat
 - tahy s kralem
 |- kral nesmi tahnout do sachu
 - tahy s pinclem
 |- meneni pescu za nove figury (automaticky za damu)
"""

turn_time = 1

# Main

# init
game = Chess.Game()
game.NewGame()
game.PrintBord()

# set player
game.SetPlayer(AI_random.Player("black"), "black")
game.SetPlayer(AI.Player("white"), "white")

print()
# game
while game.Playing() == True:
	# white
	bord = game.bord
	move = game.player_white.Move(bord)
	if move == None:
		# nezahral
		# TODO
		if game.IsPat("white") != True:
			game.player_white.check = True
		break
	else:
		move_from = move[0]
		move_to = move[1]
		valid = game.EvaluateMove("white", move_from, move_to)
		if valid == False:
			print("Invalid move!")
			break
	game.PrintBord()
	time.sleep(turn_time/2)
	
	if game.Playing() == False:
		break
	# black
	move = game.player_black.Move(bord)
	if move == None:
		# nezahral
		if game.IsPat("black") != True:
			game.player_black.check = True
			print("Black - check set true")
		break
	else:
		move_from = move[0]
		move_to = move[1]
		valid = game.EvaluateMove("black", move_from, move_to)
		if valid == False:
			print("Invalid move!")
			break
	game.PrintBord()
	time.sleep(turn_time/2)

# Konec hry
if game.pat == True:
	print("Pat!")
else:
	print("Game won", ("black", "white")[game.Won("white")], "player!")

"""
print("\u0420\u043e\u0441\u0441\u0438\u044f")

"""