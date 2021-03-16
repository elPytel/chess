# By Pytel
import Chess
import AI
import Kubik

"""
Sachy
Generator desky
validace tahu
tahy s pinclem
tahy s kralem
kral nesmi tahnout v sachu
sach
upravit sach-mat
garde

Tahy pescem
Tahy kralem

# DONE
 - sach-mat
"""


# Main

# init
game = Chess.Game()
game.NewGame()
game.PrintBord()

# set player
game.SetPlayer(Kubik.Player("black"), "black")
game.SetPlayer(AI.Player("white"), "white")

print()
# game
while game.Playing() == True:
	# white
	move = game.player_white.Move(game.bord)
	move_from = move[0]
	move_to = move[1]
	valid = game.EvaluateMove("white", move_from, move_to)
	if valid == False:
		print("Invalid move!")
		break
	game.PrintBord()
	
	if game.Playing() == False:
		break
	# black
	move = game.player_black.Move(game.bord)
	move_from = move[0]
	move_to = move[1]
	valid = game.EvaluateMove("black", move_from, move_to)
	if valid == False:
		print("Invalid move!")
		break
	game.PrintBord()
	
#if game.Won("white"):
print("Game won", ("black", "white")[game.Won("white")], "player!")

"""
print("\u0420\u043e\u0441\u0441\u0438\u044f")

"""