from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
	terminal = game_state.is_terminal()  #this will check if current state is a terminal state 
	if (depth==0) or (terminal):
		newScores = game_state.get_scores(terminal)
		return newScores, None

	"""
---------ok I am going to include some psuedo code, given from a youtube video from the instructions as a "guide" to approach this:
function minimax(position, depth, alpha, beta, maximizingPlayer):
	if depth = 0 or node is terminal node:
 		newScores = game_state.get(terminal)
   		return newScores, None
	if maximizingPlayer:
 		bestValue = -infinity
   		for each child of node:
     			value = minimax(child, depth, -1, alpha, beta, FALSE)
			bestValue = max(bestValue, value)
   			alpha = max(alpha, value)
      			if beta <= alpha
	 			break
		return bestValue, best_move
 
   	else:
    		bestValue = +infinity
      		for each child of node:
			value = minimax(child, depth, -1, alpha, beta, TRUE)
   			bestValue = min(bestValue, value)
      			if beta <= alpha
	 			break
      		return bestValue, best_move

---------The following should be our final code to that we will uncomment when ready: 
  if maximizingPlayer:
    Value = float('-inf')
    best_Move = None  # Initialize best move
    for move in game_state.get_moves():
      new_state = game_state.get_new_state(move)
      Current_value = minimax(new_state, depth - 1, False, alpha, beta)
      if Current_value > Value:
        Value = Current_value
        best_Move = move
      alpha = max(alpha, Current_value)
      if beta <= alpha:
        break
    return Value, best_Move
  else:
    Value = float('inf')  # Initialize best value for MIN
    best_Move = None  # Initialize best move
    for move in game_state.get_moves():
      new_state = game_state.get_new_state(move)
      Current_value = minimax(new_state, depth - 1, True, alpha, beta)
      if Current_value < Value:
        Value = Currrent_value
        best_Move = move
      beta = min(beta, value)
      if beta <= alpha:
        break
    return Value, best_Move

  
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()  #this will check if current state is a terminal state 
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
------------------------ The line of code under is final, when ready to uncomment--------------

	Value = float ('-inf') #both max and min are treated as max and need worst possible
 	best_Move = None

  
	return Value, best_Move


    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
    #return value, best_move
