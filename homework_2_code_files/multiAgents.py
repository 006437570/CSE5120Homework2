from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
	terminal = game_state.is_terminal()  #this will check if current state is a terminal state 
	if (depth==0) or (terminal):
		newScores = game_state.get_scores(terminal)
		return newScores, None

	"""
 YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    """

    if maximizingPlayer:
        Value = float('-inf')
        best_Move = None  # Initialize best move
        for move in game_state.get_moves():
            new_state = game_state.get_new_state(move)
            Current_value, _ = minimax(new_state, depth - 1, False, alpha, beta)
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
            Current_value, _ = minimax(new_state, depth - 1, True, alpha, beta)
            if Current_value < Value:
                Value = Current_value
                best_Move = move
            beta = min(beta, Value)
            if beta <= alpha:
                break
        return Value, best_Move
  

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()  #this will check if current state is a terminal state 
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
------------------------ The line of code under is final, when ready to uncomment--------------

	Value = float('-inf') #both max and min are treated as max and need worst possible
 	best_Move = None

  	for move in game_status.get_moves():
   		new_state = game_status.get_new_state(move)
     		Current_value = -negamax(new_state, depth -1, -turn_multiplier, -alpha, -beta)
       		if Current_value > Value:
	 		Value = Current_value
    			best_Move = move
       		alpha = max(alpha, Current_value)
	 	if beta <= alpha:
   			break
      
	return Value, best_Move


    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    
    """
