# By Pytel

import time

import Chess
import AI

"""
Sachy

# TODO
tahy s pinclem
tahy s kralem

brani mimochodem

meneni pescu za nove figury (automaticky za damu)

# DONE
 - Generator desky
 - validace tahu
 - sach
 - sach-mat
 - garde
 - kral nesmi tahnout do sachu
"""

turn_time = 0.8

# Main

# init
game = Chess.Game()
game.NewGame()
game.PrintBord()

# set player
game.SetPlayer(AI.Player("black"), "black")
game.SetPlayer(AI.Player("white"), "white")

print()
# game
while game.Playing() == True:
	# white
	bord = game.bord
	move = game.player_white.Move(bord)
	if move == None:
		# nezahral
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
	
#if game.Won("white"):
print("Game won", ("black", "white")[game.Won("white")], "player!")

"""
print("\u0420\u043e\u0441\u0441\u0438\u044f")

"""