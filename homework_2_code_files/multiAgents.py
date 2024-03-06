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
 	if maximizingPlayer:   #conditional statement to first check if it will be our MAX player
   		bestValue = float('-inf') #if its MAX, it must be set to the worst possible
  	return best_value, best_move
   
   	else:  # If not our MAX player
    		bestValue = float('inf') #if its MIN, it must be set to best possible
    	return best_value, best_move

  
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """

	# return value, best_move

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()  #this will check if current state is a terminal state 
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
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
