# -*- coding: utf-8 -*-


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state #The tic tac toe game board
		self.turn_O = turn_O #Bool that tracks if its the 'O' player's turn or not
		self.oldScores = 0

		self.winner = "" #Winning player of current game

	#FINISHED?
	def is_terminal(self):
		"""
        YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
        THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER 
        """
		moves = self.get_moves() #List of available moves
		#if there are no more availble moves calculate winning player and return True
		if len(moves) == 0:
			if (self.get_scores(True) < 0):
				self.winner = "(X)"
			elif (self.get_scores(True) > 0):
				self.winner = "(O)"
			else:
				self.winner = "Draw"
			return True, self.winner
		#If there are still available moves, then return False.
		return False, None

	#FINSHED?
	def get_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
        EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
        
        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
        NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
        
        """        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2 #if game is over, then 3 in a row is needed.

		#Calc the score if the game is over
		if check_point == 3: 
			#Check vertical score
			for i in range(cols):
				for j in range(cols-2): #at a certain point it is impossible to get 3 in a row. 'cols-2' addresses that
					if self.board_state[j][i] == self.board_state[j+1][i] == self.board_state[j+2][i] != 0:
						scores+=self.board_state[j][i]
						#print("Vert point",self.board_state[j][i])

			#Check horizontal score
			for i in range(rows):
				for j in range(rows-2):
					if self.board_state[i][j] == self.board_state[i][j+1] == self.board_state[i][j+2] != 0:
						scores+=self.board_state[i][j]
						#print("Horiz Point",self.board_state[i][j])

			#Check diagonal down score
			for i in range(cols-2):
				for j in range(cols-2):
					if self.board_state[i][j] == self.board_state[i+1][j+1] == self.board_state[i+2][j+2] != 0:
						scores+=self.board_state[i][j]
						#print("Diag Down Point", self.board_state[i][j])

			#Check diagonal up score
			for i in range(cols-2):
				for j in range(cols-1, 1,-1):
					if self.board_state[i][j] == self.board_state[i+1][j-1] == self.board_state[i+2][j-2] != 0:
						scores+=self.board_state[i][j]
						#print("Diag Up Point", self.board_state[i][j])
		
		#Calc score if the game is in progress
		if check_point == 2:
			#Check vertical score
			for i in range(cols):
				for j in range(cols-1):
					if self.board_state[j][i] == self.board_state[j+1][i] != 0:
						scores+=self.board_state[j][i]
						#print("Vert point",self.board_state[j][i])

			#Check horizontal score
			for i in range(rows):
				for j in range(rows-1):
					if self.board_state[i][j] == self.board_state[i][j+1] != 0:
						scores+=self.board_state[i][j]
						#print("Horiz Point",self.board_state[i][j])

			#Check diagonal down score
			for i in range(cols-1):
				for j in range(cols-1):
					if self.board_state[i][j] == self.board_state[i+1][j+1] != 0:
						scores+=self.board_state[i][j]
						#print("Diag Down Point", self.board_state[i][j])

			#Check diagonal up score
			for i in range(cols-1):
				for j in range(cols-1, 0,-1):
					if self.board_state[i][j] == self.board_state[i+1][j-1] != 0:
						scores+=self.board_state[i][j]
						#print("Diag Up Point", self.board_state[i][j])

		return scores

	#NOT FINISHED!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
	    

	#FINISHED???????????????????
	#code for finding available moves
	def get_moves(self):
		moves = [] #List of unplayed moves
		# Loops through each value in the current board state
		for x in range(len(self.board_state)):
			for y in range(len(self.board_state)):
				if (self.board_state[x][y] == 0): # 0 means that the move has not been played yet
					moves.append([y,x]) #Adds the unplayed move to the list of unplayed moves
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
		return moves #Return the list of unplayed moves

	#FINISHED
	#Updates tictactoe board based on the most recent move made
	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[y][x] = 1 if self.turn_O else -1
		#print("This is the new board state:",new_board_state)
		return GameStatus(new_board_state, not self.turn_O)