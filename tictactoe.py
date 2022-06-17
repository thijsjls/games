world = [' ' for i in range(9)]

userworld = [i for i in range(9)]

def print_world(world):	
	form = ''' 
		| %s | %s | %s |
	    \t-------------
		| %s | %s | %s |
	    \t-------------
	    \t| %s | %s | %s |
	    '''
	print(form % tuple(world[0:3] + world[3:6] + world[6:9]))

def place_token(world, userworld, player):
	position = int(input('Enter position: '))
	while world[position] != ' ':
		position = int(input('Please enter an open position: '))
	world[position] = player[1]

def check_win(world, token):
	win = False
	# horizontaal
	if world[0:3] == [token, token, token]:
		win = True
	elif world[3:6] == [token, token, token]:
		win = True
	elif world[6:9] == [token, token, token]:
		win = True
	# verticaal
	elif world[0] == token and world[3] == token and world[6] == token:
		win = True
	elif world[1] == token and world[4] == token and world[7] == token:
		win = True
	elif world[2] == token and world[5] == token and world[8] == token:
		win = True
	# diagonaal
	elif world[0] == token and world[4] == token and world[8] == token:
		win = True
	elif world[2] == token and world[4] == token and world[6] == token:
		win = True
	return win

def turn(world, userworld, player):
	print('Dear ' + player[0] + ' the world now looks like this:')
	print_world(world)
	print('Please enter a position number as indicated below to place your token.')
	print_world(userworld)
	place_token(world, userworld, player)

def main():
	print('\n\n\n\n\n\n                                   Tic Tac Toe')
	print('                       a Python based game by Thijs Sluijter\n\n')	
	print('   This program contains an implementation of the popular game Tic Tac Toe\n\n')
	player1name = input('Player 1 please enter your name: ')
	player2name = input('Player 2 please enter your name: ')
	player1 = (player1name, 'x')
	player2 = (player2name, 'o')
	print(player1[0] + ' starts')

	turns = 0
	while True:
		print(turns)
		turn(world, userworld, player1)
		turns += 1
		if check_win(world, player1[1]):
			print(player1[0] + ' wins')
			break
		if turns >= 9:
			print('It\'s a draw...')
			break
		turn(world, userworld, player2)
		turns += 1
		if check_win(world, player2[1]):
			print(player2[0] + ' wins')
			break
		if turns >= 9:
			print('It\'s a draw...')
			break

	print('Thanks for playing! Please type "python tictactoe.py" and press ENTER to play again.')

if __name__ == "__main__":
	main()
