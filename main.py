# By Pytel
import Chess
import AI

"""
Sachy
Generator desky
validace tahu
tahy s pinclem
tahy s kralem
kral nesmi tahnout v sachu
sach
sach-mat
garde
"""


# Main

# init
game = Chess.Game()
game.PrintChessmans()
print()
game.NewGame()
game.PrintBord()

# set player
game.SetPlayer(AI.Player("black", game), "black")
game.SetPlayer(AI.Player("white", game), "white")

print()
# game
while game.Playing() == True:
	# white
	move = game.player_white.Move()
	move_from = move[0]
	move_to = move[1]
	valid = game.EvaluateMove("white", move_from, move_to)
	if valid == False:
		print("Invalid move!")
		break
	game.PrintBord()
	# black
	move = game.player_black.Move()
	move_from = move[0]
	move_to = move[1]
	valid = game.EvaluateMove("white", move_from, move_to)
	if valid == False:
		print("Invalid move!")
		break
	game.PrintBord()

"""
print("\u0420\u043e\u0441\u0441\u0438\u044f")

"""