#tic tac toe from scratch
# Prints the entire board out, it asks for the arguements of a list in the range 1 - 9
def game_board(position):
	print('\n')
	print(position[7] + ' | ' + position[8] + ' | ' + position[9])
	print(position[4] + ' | ' + position[5] + ' | ' + position[6])
	print(position[1] + ' | ' + position[2] + ' | ' + position[3])
	print('\n')

# Asks the player if they want to b X's or O's. then returns a tuple in the order.
# I do this because i will then assign the player1 and player2 like so player1,player2 = player_input() 
# The player input function returns the list and then assigned the variables.
def player_input():
	answer = input('Choose a piece (X or O): ')

	if answer.lower() == 'x':
		return ('X','O')
	else:
		return ('O','X')


# This functions just returns in the number what the user puts in.
# I am not returning a variable, because then i wouldn't be prompted for the users input
def pick_spot_on_the_board():
	return int(input('Pick a spot on the board (1-9): '))
	

# The functions asks for 2 arguements, 
# It then takes the varible Board_positions which is usally set to 10 x ' '
# It then replaces the position given with the player, so if you pass in player1 and they chose X, it will replace the blank space with the player icon
# It then returns the new up to date board_positions variable, overwriting the previous empty one.
def place_marker(position,player):
	board_positions[position] = player
	return board_positions
	
# This simply checks to see if any 3 in a rows are made in order
def check_winner(board_placements):
	return (board_positions[1] == 'X' and board_positions[2] == 'X' and board_positions[3] == 'X' or 
			board_positions[4] == 'X' and board_positions[5] == 'X' and board_positions[6] == 'X' or 
			board_positions[7] == 'X' and board_positions[8] == 'X' and board_positions[9] == 'X' or
			board_positions[1] == 'X' and board_positions[4] == 'X' and board_positions[7] == 'X' or
			board_positions[2] == 'X' and board_positions[5] == 'X' and board_positions[8] == 'X' or
			board_positions[3] == 'X' and board_positions[6] == 'X' and board_positions[9] == 'X' or
			board_positions[1] == 'X' and board_positions[5] == 'X' and board_positions[9] == 'X' or
			board_positions[3] == 'X' and board_positions[5] == 'X' and board_positions[7] == 'X' or
			board_positions[1] == 'O' and board_positions[2] == 'O' and board_positions[3] == 'O' or 
			board_positions[4] == 'O' and board_positions[5] == 'O' and board_positions[6] == 'O' or 
			board_positions[7] == 'O' and board_positions[8] == 'O' and board_positions[9] == 'O' or
			board_positions[1] == 'O' and board_positions[4] == 'O' and board_positions[7] == 'O' or
			board_positions[2] == 'O' and board_positions[5] == 'O' and board_positions[8] == 'O' or
			board_positions[3] == 'O' and board_positions[6] == 'O' and board_positions[9] == 'O' or
			board_positions[1] == 'O' and board_positions[5] == 'O' and board_positions[9] == 'O' or
			board_positions[3] == 'O' and board_positions[5] == 'O' and board_positions[7] == 'O'
			)

# This functions checks to see if the position is blank, if it isn't blank and has already been picked by a player,
# then the function will return False rather than True
def check_space(board_positions,position):
	return board_positions[position] == ' '

# replay returns the value of yes or no question
def replay():
	return input('want to replay? Yes or No?: ').lower()


#############################################################################
# This was my first attempt but got completely lost and started again

# board_positions = list(' ' * 10)
# player1,player2 = player_input()
# spot_chosen = pick_spot_on_the_board()

# flag = True
# turn = True

# while flag:
# 	if turn == True:
# 		pick_spot_on_the_board()
# 		place_marker(spot_chosen,player1)
# 		print(game_board(board_positions))
# 		turn = False
# 	else:
# 		pick_spot_on_the_board()
# 		place_marker(spot_chosen,player1)
# 		print(game_board(board_positions))
# 		turn = True



###############################################################################




#  Start of the game.
# Board positions variable is set to a list with 10 empty spaces
board_positions = list(' ' * 10)
# As stated before, player1 and player2 variables are assigned in order of the return of (X,O)
player1,player2 = player_input()
# This flag is for if the user wants to replay, if it is set to True than the game will continue
game_on = True
# This flag is for who's turn it is, because there is only 2 users, i can simply use True and false
turn = True
# While the game_on variable is True we will loop the game.
while game_on:
	# If the turn is True, which by default it is, we will start with player1's turn.
	if turn:
		#To start with, the game checks if the theres a winner, using the function check_winner and passing in the board_positions.
		if check_winner(board_positions):
			# If there is a winner, it prints off who won, player2 won because it checks at the beggining of the opponents turn, rather than the end of there turn.
			print(player2 + ' Wins!')
			# Asks the user if they want to replay.
			replay()
			# If the user inputs 'yes' then the bord positions will be overwritten with all blank spaces again and loop, the check_winner will go to False because there
			# are no matching positions anymore.
			if replay() == 'yes':
				board_positions = list(' ' * 10)
			else:
				# Else it will break the while loop
				break
		else:
			# if there is no winner, the varible spot is assigned, which asks the user to input a number, and replaces the spot variable with the up to date number
			spot = pick_spot_on_the_board()
			# It now calls the function check_space with the arguements board_positions and the spot variable i just assigned.#
			# This function checks to see in the list[spot] and position of spot if the value is ' ' and not anything else.
			# If it is anything but ' ' it will loop and just ask the user to put a number in again.
			if check_space(board_positions,spot) == True:
				# If it is an empty space, it calls the function place_marker with the number and player icon.
				# It will update the list position with the players icon. so for example it will look something like:
				# [' ',' ',' ',' ','X',' ',' ',' ',' ']
				place_marker(spot,player1)
				# The function gameboard is then called, all this does is print the board with the updated board_positions variable.
				game_board(board_positions)
				# We then change the turn to False, which passes it the next player, because if we didn't do this then the program will loop on the same turn.
				# And we will loop this same section with the variable player1 instead of player2's variable which is set to the opposite marker.
				# by this i mean the variables at the beggining player1,player2 = ('X','O')
				turn = False
			else:
				#This is the else statement for the check_space function
				game_board(board_positions)
	# because game_on is still True, we loop and because turn is no longer True, we run the else statement of the if statement.	
	else:
		#This is the exact same thing except with player1's icon, we will user player2's icon, and repeat the process.
		if check_winner(board_positions):
			print(player1 + ' Wins!')
			replay()
			if replay() == 'yes':
				board_positions = list(' ' * 10)
			else:
				break
		else:
			spot = pick_spot_on_the_board()
			if check_space(board_positions,spot) == True:
				place_marker(spot,player2)
				game_board(board_positions)
				turn = True
			else:
				game_board(board_positions)

