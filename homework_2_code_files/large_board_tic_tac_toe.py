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
        self.game_state = GameStatus(board_state=[],turn_O=True)

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
        self.GRID_SIZE = 4
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        #Modified self.HEIGHT, to consider the GUI_HEIGHT so the grid remains square despite a non-square window size
        self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Option select values for GUI
        self.screenSizeOption = 0
        
        # Boolean for AI Negamax/Minimax option select
        self.aiSelectNegamax = True

        # Initialize pygame
        pygame.init()
        self.game_reset()

    #NOT FINISHED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
        self.gridResizeButton3 = pygame.Rect((self.width - 105, (self.GUI_HEIGHT/2)-15), (25,25))
        pygame.draw.rect(self.screen, self.BLUE, self.gridResizeButton3, 0, 2)
        self.gridResizeButton4 = pygame.Rect((self.width - 70, (self.GUI_HEIGHT/2)-15), (25,25))
        pygame.draw.rect(self.screen, self.BLUE, self.gridResizeButton4, 0 , 2)
        self.gridResizeButton5 = pygame.Rect((self.width - 35,(self.GUI_HEIGHT/2)-15), (25,25))
        pygame.draw.rect(self.screen, self.BLUE, self.gridResizeButton5, 0, 2)
        
        #Draw box to show current grid size selection
        if self.GRID_SIZE == 3:
            pygame.draw.rect(self.screen, self.WHITE, self.gridResizeButton3, 2, 2)
        elif self.GRID_SIZE == 4:
            pygame.draw.rect(self.screen, self.WHITE, self.gridResizeButton4, 2, 2)
        elif self.GRID_SIZE == 5:
            pygame.draw.rect(self.screen, self.WHITE, self.gridResizeButton5, 2, 2)

        # Buttons that lets user select desired game mode (human vs human/human vs computer)
        self.pvpButton = pygame.draw.circle(self.screen, self.BLUE, (22, 25), 7, 0)
        self.pvaButton = pygame.draw.circle(self.screen, self.BLUE, (22, 44), 7, 0)
        # Draw dot to show current game mode selection
        if mode == "player_vs_ai":
            pygame.draw.circle(self.screen, self.BLACK, (self.pvaButton.centerx,self.pvaButton.centery), 4, 0)
        else:
            pygame.draw.circle(self.screen, self.BLACK, (self.pvpButton.centerx,self.pvpButton.centery), 4, 0)
        
        # Button to select AI negamax or minimax
        self.negamaxButton = pygame.draw.circle(self.screen, self.BLUE, (22, (self.GUI_HEIGHT/2)+8), 7, 0)
        self.minimaxButton = pygame.draw.circle(self.screen, self.BLUE, (22, (self.GUI_HEIGHT/2)+27), 7, 0)
        #Draw dot to show current AI algorithm selection
        if self.aiSelectNegamax:   
            pygame.draw.circle(self.screen, self.BLACK, (self.negamaxButton.centerx,self.negamaxButton.centery), 4, 0)
        else:
            pygame.draw.circle(self.screen, self.BLACK, (self.minimaxButton.centerx,self.minimaxButton.centery), 4, 0)
            
        # Buttons for user to select if they want to draw a cross or nought
        self.noughtButton = pygame.draw.circle(self.screen, self.BLUE, (22, self.GUI_HEIGHT-10), 7, 0)
        self.crossButton = pygame.draw.circle(self.screen, self.BLUE, (66, self.GUI_HEIGHT-10), 7, 0)
        #Draw dot to show symbol selection
        if self.game_state.turn_O:
            pygame.draw.circle(self.screen, self.BLACK, (self.noughtButton.centerx,self.noughtButton.centery), 4, 0)
        else:
            pygame.draw.circle(self.screen, self.BLACK, (self.crossButton.centerx,self.noughtButton.centery), 4, 0)
            
        
        #Buttons to change window size
        self.smallResolutionButton = pygame.Rect((self.width - 105, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLACK, self.smallResolutionButton, 0, 2)
        self.mediumResolutionButton = pygame.Rect((self.width - 70, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLACK, self.mediumResolutionButton, 0, 2)
        self.largeResolutionButton = pygame.Rect((self.width - 35, 10), (25,25))
        pygame.draw.rect(self.screen, self.BLACK, self.largeResolutionButton, 0, 2)
        
        #Draw square to show screen size selection
        if self.screenSizeOption == 0:
            #Draw square to show small screen selection
            pygame.draw.rect(self.screen, self.WHITE, self.smallResolutionButton, 2, 2)
        elif self.screenSizeOption == 1:
            #Draw square to show medium screen selection
            pygame.draw.rect(self.screen, self.WHITE, self.mediumResolutionButton, 2, 2)
        elif self.screenSizeOption == 2:
            #Draw square to show large screen selection
            pygame.draw.rect(self.screen, self.WHITE, self.largeResolutionButton, 2, 2)    
        
        
        #Display Screen for Instructions, information for which symbol is playing, and results
        self.displayRect = pygame.Rect(((self.width/3), 5), ((self.width/3), self.GUI_HEIGHT-60))
        pygame.draw.rect(self.screen, (160, 171, 192), self.displayRect, 0, 2)
        pygame.draw.rect(self.screen, (50,50,50), self.displayRect, 3, 2)
        
        self.scoreRect = pygame.Rect(((self.width/3), self.GUI_HEIGHT - 54), ((self.width/3), (self.GUI_HEIGHT/3)-(8*self.screenSizeOption)))
        pygame.draw.rect(self.screen, (160, 171, 192), self.scoreRect, 0, 2)
        pygame.draw.rect(self.screen, (50,50,50), self.scoreRect, 3, 2)
        

        #Text for GUI=========================================================================
        #Text Font
        self.text_font = pygame.font.SysFont("calibri", 14, bold = True)
        
        #Game Mode text
        imgGameModeText = self.text_font.render("Game Mode:", self.text_font, self.BLACK)
        self.screen.blit(imgGameModeText, (self.pvpButton.topleft[0], self.pvpButton.topleft[1]-16))
        #PvP Text
        imgPvpText = self.text_font.render("Player vs Player", self.text_font, self.BLACK)
        self.screen.blit(imgPvpText, (self.pvpButton.right+5, self.pvpButton.topleft[1]))
        #PvAI Text
        imgPvaText = self.text_font.render("Player vs AI", self.text_font, self.BLACK)
        self.screen.blit(imgPvaText, (self.pvaButton.right+5, self.pvaButton.topleft[1]))
        
        #AI Algorithm text
        imgAIModeText = self.text_font.render("AI Algorithm:", self.text_font, self.BLACK)
        self.screen.blit(imgAIModeText, (self.negamaxButton.topleft[0], self.negamaxButton.topleft[1]-16))
        #Negamax Text
        imgNegamaxText = self.text_font.render("Negamax", self.text_font, self.BLACK)
        self.screen.blit(imgNegamaxText, (self.negamaxButton.right+5, self.negamaxButton.topleft[1]))
        #Minimax Text
        imgMinimaxText = self.text_font.render("Minimax", self.text_font, self.BLACK)
        self.screen.blit(imgMinimaxText, (self.minimaxButton.right+5, self.minimaxButton.topleft[1]))
        
        #Symbol Select Text
        imgSymbolText = self.text_font.render("Player 1 Symbol:", self.text_font, self.BLACK)
        self.screen.blit(imgSymbolText, (self.noughtButton.topleft[0], self.GUI_HEIGHT - 34))
        #Nought symbol Text
        imgNoughtText = self.text_font.render("O", self.text_font, self.BLACK)
        self.screen.blit(imgNoughtText, (self.noughtButton.right+5, self.noughtButton.topleft[1]))
        #Cross symbol Text
        imgCrossText = self.text_font.render("X", self.text_font, self.BLACK)
        self.screen.blit(imgCrossText, (self.crossButton.right+5, self.crossButton.topleft[1]))
        
        #Start Button Text
        imgStartText = self.text_font.render("Start", self.text_font, self.BLACK)
        self.screen.blit(imgStartText, (self.startButton.centerx-14, self.startButton.centery-5))
        #Reset Button Text
        imgResetText = self.text_font.render("Reset", self.text_font, self.BLACK)
        self.screen.blit(imgResetText, (self.resetButton.centerx-15, self.resetButton.centery-5))
        
        #Screen Resolution Size Text
        imgScreenSizeText = self.text_font.render("Screen Size:", self.text_font, self.BLACK)
        self.screen.blit(imgScreenSizeText, (self.smallResolutionButton.centerx - 87, self.smallResolutionButton.centery-5))
        #Small Screen Text
        imgScreenSText = self.text_font.render("S", self.text_font, self.WHITE)
        self.screen.blit(imgScreenSText, (self.smallResolutionButton.centerx-3, self.smallResolutionButton.centery-5))
        #Medium Screen Text
        imgScreenMText = self.text_font.render("M", self.text_font, self.WHITE)
        self.screen.blit(imgScreenMText, (self.mediumResolutionButton.centerx-6, self.mediumResolutionButton.centery-5))
        #Large Screen Text
        imgScreenLText = self.text_font.render("L", self.text_font, self.WHITE)
        self.screen.blit(imgScreenLText, (self.largeResolutionButton.centerx-3, self.largeResolutionButton.centery-5))
        
        #Board Size Text
        imgBoardSizeText = self.text_font.render("Board Size:", self.text_font, self.BLACK)
        self.screen.blit(imgBoardSizeText, (self.gridResizeButton3.centerx - 84, self.gridResizeButton3.centery-5)) 
        #3x3 Board Size Text
        imgBoard3Text = self.text_font.render("3", self.text_font, self.WHITE)
        self.screen.blit(imgBoard3Text, (self.gridResizeButton3.centerx-3, self.gridResizeButton3.centery-5))
        #4x4 Board Size Text
        imgBoard4Text = self.text_font.render("4", self.text_font, self.WHITE)
        self.screen.blit(imgBoard4Text, (self.gridResizeButton4.centerx-3, self.gridResizeButton4.centery-5))
        #5x5 Board Size Text
        imgBoard5Text = self.text_font.render("5", self.text_font, self.WHITE)
        self.screen.blit(imgBoard5Text, (self.gridResizeButton5.centerx-3, self.gridResizeButton5.centery-5))
        
        #Display Text
        self.displayText = "Select Start to Play"
        imgDisplayText = self.text_font.render(self.displayText, self.text_font, self.BLACK)
        self.screen.blit(imgDisplayText, (self.displayRect.centerx-55, self.displayRect.centery-5))
        
        #Set default values for scores
        self.updateScores(0, 0)
        
        """
        GUI...
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
    
    #Custom Helper function to update player scores (Paremeters: integers for player scores)
    def updateScores(self, score1, score2):
        #Draw rectangle for score window
        self.scoreRect = pygame.Rect(((self.width/3), self.GUI_HEIGHT - 54), ((self.width/3), (self.GUI_HEIGHT/3)-(8*self.screenSizeOption)))
        pygame.draw.rect(self.screen, (160, 171, 192), self.scoreRect, 0, 2)
        pygame.draw.rect(self.screen, (50,50,50), self.scoreRect, 3, 2)
        
        #Convert integers to strings for text
        scoreText1 = str(score1)
        scoreText2 = str(score2)
        
        #Draw Player's score Text
        self.playerScoreHeaderText1 = "Player 1 Score"
        imgPlayerScoreHeaderText1 = self.text_font.render(self.playerScoreHeaderText1, self.text_font, self.BLACK)
        self.screen.blit(imgPlayerScoreHeaderText1, (self.scoreRect.centerx-85, self.scoreRect.centery-16))
        self.playerScoreHeaderText2 = "Player 2 Score"
        imgPlayerScoreHeaderText2 = self.text_font.render(self.playerScoreHeaderText2, self.text_font, self.BLACK)
        self.screen.blit(imgPlayerScoreHeaderText2, (self.scoreRect.centerx+8, self.scoreRect.centery-16)) 
        self.playerScoreText1 = scoreText1
        imgPlayerScoreText1 = self.text_font.render(self.playerScoreText1, self.text_font, self.BLACK)
        self.screen.blit(imgPlayerScoreText1, (self.scoreRect.centerx-47, self.scoreRect.centery+1))
        self.playerScoreText2 = scoreText2
        imgPlayerScoreText2 = self.text_font.render(self.playerScoreText2, self.text_font, self.BLACK)
        self.screen.blit(imgPlayerScoreText2, (self.scoreRect.centerx+46, self.scoreRect.centery+1))
        

    #Basically just changes the title of the window based on who's turn it is
    def change_turn(self):
        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")
            
        #Update Display Text
        if self.game_state.turn_O:
            self.displayText = "O's Turn"
        else:
            self.displayText = "X's Turn"
        pygame.draw.rect(self.screen, (160, 171, 192), self.displayRect, 0, 2)
        pygame.draw.rect(self.screen, (50,50,50), self.displayRect, 3, 2)
        imgDisplayText = self.text_font.render(self.displayText, self.text_font, self.BLACK)
        self.screen.blit(imgDisplayText, (self.displayRect.centerx-25, self.displayRect.centery-5)) 

    #FINSIHED
    def draw_circle(self, x, y):
        # Draws a circle at the center of the block
        pygame.draw.circle(self.screen, self.BLUE, (x,y+self.GUI_HEIGHT), self.WIDTH/2, 5)
        
    # FINSIHED
    def draw_cross(self, x, y):
        # Draws 2 diagonal lines that reach from one corner of a grid cell 
        # to the other. 
        for i in range(5): #loops to give the line some added thickness
            pygame.draw.aaline(self.screen, self.RED, (x+i, y+self.GUI_HEIGHT), ((self.WIDTH+x+i)-self.MARGIN, self.WIDTH+y+self.GUI_HEIGHT))
            pygame.draw.aaline(self.screen, self.RED, ((self.WIDTH+x+i)-self.MARGIN, y+self.GUI_HEIGHT), (x+i, self.HEIGHT+y+self.GUI_HEIGHT))

    # FINISHED??????????????????????????????????????
    def is_game_over(self):
        if self.game_state.is_terminal()[0]:
            return True
        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
    
    #IDK WHAT THE PURPOSE OF THIS IS???
    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)

    # NOT FINISHED VERY IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        if self.aiSelectNegamax:
            print("Using Negamax Algorithm")
        else:
            print("Using Minimax Algorithm")
        
        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """


    #FINISHED???????????????????????????????
    def game_reset(self):
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        # 2D array that will hold all the data of the tic-tac-toe game
        # Loop will initialize the game board to the correct size and with all 0's
        self.game_state.board_state=[]
        for row in range(self.GRID_SIZE):
            self.game_state.board_state.append([])
            for column in range(self.GRID_SIZE):
                self.game_state.board_state[row].append(0) #places 0 in all places to indicate an unplayed position
        print(np.array(self.game_state.board_state))
        
        pygame.display.update()

    #NOT FINSHED!!!!!!!!!!!!!!!!!!!!!!!!!
    #As the name suggests, this the the function kinda controls how the game is run
    def play_game(self, mode = "player_vs_ai"):
        done = False
        gameStarted = False #Bool that tracks if game has started for certain game settings

        clock = pygame.time.Clock() #idk what this is for?

        #Loop that will go on for as long as we want to play the game (this is what makes the game really run)
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
                # User clicks on something on the screen
                if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position of the mouse
                    mouseCoordinates = pygame.mouse.get_pos()
                    print(mouseCoordinates)

                    # Change the x/y screen coordinates to grid coordinates
                    selectedX = int(mouseCoordinates[0]//(self.width//self.GRID_SIZE))
                    selectedY = int((mouseCoordinates[1] - self.GUI_HEIGHT)//(self.width//self.GRID_SIZE))
                    print("Grid clicked at:", [selectedX, selectedY])

                    # Buttons only work if a game isn't in progress
                    if not gameStarted:
                        # User starts the game and can now start clicking on the grid
                        if self.startButton.collidepoint(mouseCoordinates):
                            print("Starting game...")
                            gameStarted = True

                        """
                        #This is code that allows us to increase the size of the window.
                        """
                        if self.smallResolutionButton.collidepoint(mouseCoordinates):
                            self.width = 600
                            self.height = 750
                            self.size = self.width, self.height
                            self.GUI_HEIGHT = self.size[1]-self.size[0]
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            self.screenSizeOption = 0
                            tictactoegame.game_reset()
                        if self.mediumResolutionButton.collidepoint(mouseCoordinates):
                            self.width = 700
                            self.height = 875
                            self.size = self.width, self.height
                            self.GUI_HEIGHT = self.size[1]-self.size[0]
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            self.screenSizeOption = 1
                            tictactoegame.game_reset()
                        if self.largeResolutionButton.collidepoint(mouseCoordinates):
                            self.width = 800
                            self.height = 1000
                            self.size = self.width, self.height
                            self.GUI_HEIGHT = self.size[1]-self.size[0]
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            self.screenSizeOption = 2
                            tictactoegame.game_reset()

                        """
                        # Buttons that increases the size of the grid
                        # Wont work if the game has been started to not mess with any existing game
                        """
                        if self.gridResizeButton3.collidepoint(mouseCoordinates):
                            self.GRID_SIZE = 3
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset() #redraw the board to update size
                        if self.gridResizeButton4.collidepoint(mouseCoordinates):
                            self.GRID_SIZE = 4
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset() # redraw board to update size 
                        if self.gridResizeButton5.collidepoint(mouseCoordinates):
                            self.GRID_SIZE = 5
                            self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
                            self.HEIGHT = (self.size[1]-self.GUI_HEIGHT)/self.GRID_SIZE - self.OFFSET
                            tictactoegame.game_reset() #redraw board to update size  
                            

                        # Buttons to swap between game modes
                        if self.pvpButton.collidepoint(mouseCoordinates):
                            print("Activating PvP:")
                            mode = "player_vs_player"
                            #Draw dot for PvP Option
                            pygame.draw.circle(self.screen, self.BLACK, (self.pvpButton.centerx,self.pvpButton.centery), 4, 0)
                            #"Erase" Dot on PvA Option
                            pygame.draw.circle(self.screen, self.BLUE, (22, 44), 7, 0)
                        if self.pvaButton.collidepoint(mouseCoordinates):
                            print("Activating PvC:")
                            mode = "player_vs_ai"
                            #Draw dot for PvA Option
                            pygame.draw.circle(self.screen, self.BLACK, (self.pvaButton.centerx,self.pvaButton.centery), 4, 0)
                            #"Erase" Dot for PvP Option
                            pygame.draw.circle(self.screen, self.BLUE, (22, 25), 7, 0)
                        
                        #Buttons to switch Negamax or Minimax Algorithms
                        if self.negamaxButton.collidepoint(mouseCoordinates):
                            print("Negamax Algorithm Selected")
                            self.aiSelectNegamax = True
                            #Draw dot for Negamax
                            pygame.draw.circle(self.screen, self.BLACK, (self.negamaxButton.centerx,self.negamaxButton.centery), 4, 0)
                            #"Erase" minimax dot
                            pygame.draw.circle(self.screen, self.BLUE, (22, (self.GUI_HEIGHT/2)+27), 7, 0)
                        if self.minimaxButton.collidepoint(mouseCoordinates):
                            print("Minimax Algorithm Selected")
                            self.aiSelectNegamax = False
                            #Draw dot for minimax
                            pygame.draw.circle(self.screen, self.BLACK, (self.minimaxButton.centerx,self.minimaxButton.centery), 4, 0)
                            #"Erase" negamax dot
                            pygame.draw.circle(self.screen, self.BLUE, (22, (self.GUI_HEIGHT/2)+8), 7, 0)

                        # Buttons to swap between nought or cross
                        if self.noughtButton.collidepoint(mouseCoordinates):
                            print("Switching to nought (O)")
                            self.game_state.turn_O = True
                            #Draw dot to show O selection
                            pygame.draw.circle(self.screen, self.BLACK, (self.noughtButton.centerx,self.noughtButton.centery), 4, 0)
                            #"Erase" dot for X selection
                            pygame.draw.circle(self.screen, self.BLUE, (66, self.GUI_HEIGHT-10), 7, 0)
                        if self.crossButton.collidepoint(mouseCoordinates):
                            print("Switching to cross (X)")
                            self.game_state.turn_O = False
                            #Draw dot to show X Selection
                            pygame.draw.circle(self.screen, self.BLACK, (self.crossButton.centerx,self.crossButton.centery), 4, 0)
                            #"Erase" dot for O Selection
                            pygame.draw.circle(self.screen, self.BLUE, (22, self.GUI_HEIGHT-10), 7, 0)

                    #Buttons that work if a game is in progress
                    if gameStarted:
                        if self.game_state.turn_O:
                            player1, player2 = 1, -1
                        else:
                            player1, player2 = -1, 1
                        print("Player 1:",player1)
                        print("Player 2:", player2)
                            
                        #Change window caption if the game has started
                        tictactoegame.change_turn()

                        # If game hasn't started yet, but user hits start button, then let user know
                        if self.startButton.collidepoint(mouseCoordinates):
                            print("Game already started...")
                            

                        # Clears the grid, only works if the user has started the game, as it would be redundant other wise
                        if self.resetButton.collidepoint(mouseCoordinates):
                            print("Reseting game...")
                            gameStarted = False
                            tictactoegame.game_reset()

                    # if a game has started and the player selectes a valid grid space
                    if selectedX < self.GRID_SIZE and 0 <= selectedY < self.GRID_SIZE and gameStarted == True:
                        #if the selected grid hasn't been choosen yet, then...
                        availableMoves = self.game_state.get_moves()
                        #print("AvalavailableMoves:", availableMoves)
                        if ([selectedX, selectedY]) in availableMoves:
                            # If user selected a 'nought' then draw circle
                            if self.game_state.turn_O:
                                tictactoegame.draw_circle(((self.MARGIN + self.WIDTH) * selectedX + self.MARGIN)+self.WIDTH/2, ((self.MARGIN + self.HEIGHT) * selectedY + self.MARGIN)+self.HEIGHT/2)
                            # If user selected a 'cross' then draw a cross
                            else:
                                tictactoegame.draw_cross((self.MARGIN + self.WIDTH) * selectedX + self.MARGIN, (self.MARGIN + self.HEIGHT) * selectedY + self.MARGIN)
                            
                            # Update tic-tac-toe board with a value
                            self.game_state.get_new_state([selectedX,selectedY])
                            print(np.array(self.game_state.board_state))

                            #Check is the game is over
                            if tictactoegame.is_game_over():
                                #Put code here to calculate scores and determine a winner
                                print("GAME IS OVER SUCKA")
                                # Update Display Text
                                # TODO: ***Change self.displayText to output winner********************************
                                self.game_state.get_scores(self.game_state.is_terminal()[0])
                                self.displayText = self.game_state.winner + " Wins!"
                                pygame.draw.rect(self.screen, (160, 171, 192), self.displayRect, 0, 2)
                                pygame.draw.rect(self.screen, (50,50,50), self.displayRect, 3, 2)
                                imgDisplayText = self.text_font.render(self.displayText, self.text_font, self.BLACK)
                                self.screen.blit(imgDisplayText, (self.displayRect.centerx-47, self.displayRect.centery-5)) 
                                break

                            #end the player's turn
                            self.game_state.turn_O = not self.game_state.turn_O
                            tictactoegame.change_turn()

                            # Check if the game is human vs human or human vs AI player from the GUI. 
                            #if the mode is player vs player, then the next player will simply start their turn
                            if mode == "player_vs_ai":
                                print("activate AI here:")
                                self.play_ai()

                        # Debugging to ensure that the user as already selected a spot on the tic-tac-toe grid
                        else:
                            print("Grid:",[selectedX,selectedY],"has already been selected...")

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