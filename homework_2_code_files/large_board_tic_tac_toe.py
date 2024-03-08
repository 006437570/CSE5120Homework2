"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 750)):

        """
        Defines the top portion of the screen to be for the GUI
        Specifically, this is used to prevent the game board grid 
        from losing its 'square' shape and allows it to be 
        separate from the GUI.
        """
        self.GUI_HEIGHT = size[1]-size[0]

        self.size = self.width, self.height = size

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255) #Added blue, so the CROSS and CIRCLES can have distinctly unique colors

        # Grid Size
        self.GRID_SIZE = 3
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        #Modified self.HEIGHT, to consider the GUI_HEIGHT so the grid remains square despite a non-square window size
        self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        self.game_reset()

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)
        """
        YOUR CODE HERE TO DRAW THE GRID OTHER CONTROLS AS PART OF THE GUI
        """

        #CODE WILL GO HERE TO DISPLAY THE GUI OPTIONS
        # Basically the background color for the GUI
        guiRect = pygame.Rect((0,0), (self.width,self.GUI_HEIGHT))
        pygame.draw.rect(self.screen, self.CIRCLE_COLOR, guiRect,0,4) #Using self.CIRCLE_COLOR for background color b/c I though it looked nice against the white grid squares

        #Start Game Button
        self.startButton = pygame.Rect((self.width - 100, self.GUI_HEIGHT - 35), (40,25))
        pygame.draw.rect(self.screen, self.GREEN, self.startButton, 0 , 2)

        #Reset Game Button
        self.resetButton = pygame.Rect((self.width-50,self.GUI_HEIGHT-35), (40,25))
        pygame.draw.rect(self.screen, self.RED, self.resetButton, 0, 2)

        #Buttons to change grid size
        self.gridResizeButton3 = pygame.Rect((self.width - 105, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLUE, self.gridResizeButton3, 0, 2)
        self.gridResizeButton4 = pygame.Rect((self.width - 70, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLUE, self.gridResizeButton4, 0 , 2)
        self.gridResizeButton5 = pygame.Rect((self.width - 35,10), (25,25))
        pygame.draw.rect(self.screen, self.BLUE, self.gridResizeButton5, 0, 2)

        # Buttons that let user select desired game mode (human vs human/human vs computer)
        self.pvpButton = pygame.draw.circle(self.screen, self.BLUE, (22, 17), 7, 0)
        self.pvcButton = pygame.draw.circle(self.screen, self.BLUE, (22, 37), 7, 0)

        # Buttons for user to select if they want to draw a cross or nought
        self.noughtButton = pygame.draw.circle(self.screen, self.BLUE, (22, self.GUI_HEIGHT-37), 7, 0)
        self.crossButton = pygame.draw.circle(self.screen, self.BLUE, (22, self.GUI_HEIGHT-17), 7, 0)

        #Buttons to change window size
        self.smallResolutionButton = pygame.Rect((self.width - 210, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLACK, self.smallResolutionButton, 0, 2)
        self.mediumResolutionButton = pygame.Rect((self.width - 175, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLACK, self.mediumResolutionButton, 0, 2)
        self.largeResolutionButton = pygame.Rect((self.width - 140, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLACK, self.largeResolutionButton, 0, 2)

        """
        Need to add code to keep track of the winner of the current game
        and to keep track of the total wins for player and AI
        """


        # Draw the grid
        # loop that will print out the blank tic tac toe board
        # 2 for loops, so it reflects a 2D array
        print("Drawing grid of size:", self.GRID_SIZE)
        for row in range(self.GRID_SIZE):
            for column in range(self.GRID_SIZE):
                # draw invidual rectangle of each grid cell
                gridRect = pygame.Rect((self.MARGIN + self.WIDTH) * column + self.MARGIN, (self.MARGIN + self.HEIGHT) * row + self.MARGIN + self.GUI_HEIGHT, self.WIDTH, self.HEIGHT)
                pygame.draw.rect(self.screen, self.WHITE, gridRect,0,2)
        
        pygame.display.update()

    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        # Draws a circle at the center of the block
        pygame.draw.circle(self.screen, self.BLUE, (x,y+self.GUI_HEIGHT), self.WIDTH/2, 5)
        

    def draw_cross(self, x, y):
        # Draws 2 diagonal lines that reach from one corner of a grid cell 
        # to the other. 
        for i in range(5): #loops to give the line some added thickness
            pygame.draw.aaline(self.screen, self.RED, (x+i, y+self.GUI_HEIGHT), ((self.WIDTH+x+i)-self.MARGIN, self.WIDTH+y+self.GUI_HEIGHT))
            pygame.draw.aaline(self.screen, self.RED, ((self.WIDTH+x+i)-self.MARGIN, y+self.GUI_HEIGHT), (x+i, self.HEIGHT+y+self.GUI_HEIGHT))

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """



    def game_reset(self):
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """

        # 2D array that will hold all the data of the tic-tac-toe game
        # Loop will initialize the game board to the correct size and with all 0's
        self.tttBoard = []
        for row in range(self.GRID_SIZE):
            self.tttBoard.append([])
            for column in range(self.GRID_SIZE):
                self.tttBoard[row].append(0) #places 0 in all places to indicate an unplayed position
        print(np.array(self.tttBoard)) #prints current state of board
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False
        gameStarted = False #Bool that tracks if game has started for certain game settings
        drawShape = 1 # Value that will fill tttBoard array

        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():  # User did something
                
                #User quits the game
                if event.type == pygame.QUIT:
                    done = True

                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                    
                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                
                if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    mouseCoord = pygame.mouse.get_pos()
                    print(mouseCoord)

                    # Change the x/y screen coordinates to grid coordinates
                    selectedCol = int(mouseCoord[0]//(self.width//self.GRID_SIZE))
                    selectedRow = int((mouseCoord[1] - self.GUI_HEIGHT)//(self.width//self.GRID_SIZE))
                    print("Grid clicked at:", [selectedCol, selectedRow])

                    if gameStarted:
                        # If game hasn't started yet, but user hits start button, then let user know
                        if self.startButton.collidepoint(mouseCoord):
                            print("Game already started...")

                        # Clears the grid, only works if the user has started the game, as it would be redundant other wise
                        if self.resetButton.collidepoint(mouseCoord):
                            print("Reseting game...")
                            gameStarted = False
                            tictactoegame.game_reset()

                    # Buttons only work if a game isn't in progress
                    if not gameStarted:
                        # User starts the game and can now start clicking on the grid
                        if self.startButton.collidepoint(mouseCoord):
                            print("Starting game...")
                            gameStarted = True

                        """
                        #This is code that allows us to increase the size of the window.
                        #Might use later to create drop down menu to resize window, but idk
                        self.width += 50
                        self.height += 50
                        self.size = self.width, self.height
                        # Buttons that increases the size of the grid
                        # Wont work if the game has been started to not mess with any existing game
                        """

                        if self.smallResolutionButton.collidepoint(mouseCoord):
                            self.width = 400
                            self.height = 500
                            self.size = self.width, self.height
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset()
                        if self.mediumResolutionButton.collidepoint(mouseCoord):
                            self.width = 600
                            self.height = 750
                            self.size = self.width, self.height
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset()
                        if self.largeResolutionButton.collidepoint(mouseCoord):
                            self.width = 800
                            self.height = 1000
                            self.size = self.width, self.height
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset()

                        if self.gridResizeButton3.collidepoint(mouseCoord):
                            self.GRID_SIZE = 3
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset() #redraw the board to update size
                        if self.gridResizeButton4.collidepoint(mouseCoord):
                            self.GRID_SIZE = 4
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset() # redraw board to update size
                        if self.gridResizeButton5.collidepoint(mouseCoord):
                            self.GRID_SIZE = 5
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset() #redraw board to update size

                        # Buttons to swap between game modes
                        if self.pvpButton.collidepoint(mouseCoord):
                            print("Activating PvP:")
                        if self.pvcButton.collidepoint(mouseCoord):
                            print("Activating PvC:")

                        # Buttons to swap between nought or cross
                        if self.noughtButton.collidepoint(mouseCoord):
                            print("Switching to nought (0)")
                            drawShape = 1
                        if self.crossButton.collidepoint(mouseCoord):
                            print("Switching to cross (X)")
                            drawShape = 2

                    # if the clicked area falls within the grid and the user has started the game...
                    if selectedCol < self.GRID_SIZE and 0 <= selectedRow < self.GRID_SIZE and gameStarted == True:
                        #if the selected grid hasn't been choosen yet...
                        if self.tttBoard[selectedRow][selectedCol] == 0:
                            """
                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            #FIND A WAY TO DETERMINE WHETHER TO DRAW A CROSS OR A CIRCLE BASED ON PLAYER TURN
                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            """
                            # Update tic-tac-toe board with the selected value
                            self.tttBoard[selectedRow][selectedCol] = drawShape
                            print(np.array(self.tttBoard))

                            # If user selected a 'nought' then draw circle
                            if drawShape == 1:
                                tictactoegame.draw_circle(((self.MARGIN + self.WIDTH) * selectedCol + self.MARGIN)+self.WIDTH/2, ((self.MARGIN + self.HEIGHT) * selectedRow + self.MARGIN)+self.HEIGHT/2)
                            # If user selected a 'cross' then draw a cross
                            elif drawShape == 2:
                                tictactoegame.draw_cross((self.MARGIN + self.WIDTH) * selectedCol + self.MARGIN, (self.MARGIN + self.HEIGHT) * selectedRow + self.MARGIN)

                        # Debugging to ensure that the user as already selected a spot on the tic-tac-toe grid
                        else:
                            print("Grid:",[selectedRow,selectedCol],"has already been selected...")
                    
                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""

#executes game
tictactoegame.play_game()