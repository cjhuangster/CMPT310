import random   
import copy
import sys

class ticTacToe:
    def __init__(self, board):
        self.board = board
        self.playerValue = ''
        self.order = 0
        
    def drawBoard(self, board):
        print(board[6], ' | ', board[7], ' | ' , board [8])
        print('_____________')
        print(board[3] , ' | ' , board[4] , ' | ' , board [5])
        print('_____________')
        print(board[0] , ' | ' , board[1] , ' | ' , board [2])
        print()
        print()

    # set move for players
    def move (self, board, letter, move):
        board[move] = letter
        
    # checks goal
    def checkWin (self, XorO, board):
        return ((board[0]==board[1]==board[2]==XorO) 
        or (board[3]==board[4]==board[5]==XorO)
        or (board[6]==board[7]==board[8]==XorO)
        or (board[0]==board[3]==board[6]==XorO)
        or (board[1]==board[4]==board[7]==XorO)
        or (board[2]==board[5]==board[8]==XorO)
        or (board[0]==board[4]==board[8]==XorO)
        or (board[2]==board[4]==board[6]==XorO))
        
    # returns a list of available moves
    def availableMoves (self, board):
        availableSpace = []
        # print("board: ", board)
        for i in board:
            # bugged, returning positions that have already been filled
            if isinstance(i, int):
                availableSpace.append(i)
        
        # print("availableSpace: ", availableSpace)
        return availableSpace
    
    def getInfo (self):
        print()
        playerLetter =''
        while playerLetter!=('X' or 'O'):
            playerLetter = input('do you want to be X or O? (input X or O):\n')
        order = 0
        while order != (1 or 2):
            order = int(input('do you want to play first or second? (input 1 or 2):\n'))
        return playerLetter, order
    
    def aGame(self):
        # order = random.randint(1, 2)
        # playerOrder = random.randint(1,2)
        # if playerOrder == 1:
        #     playerLetter = 'X'
        # else:
        #     playerLetter = 'O'       
        # print ('by random selection, you are playing as', playerLetter, 'and going', order )
        # # playerLetter, order = self.getInfo()
        numPlayOut = 11
        # if playerLetter == 'X':
        #     AILetter = 'O'
        # else:
        #     AILetter = 'X'

        ticTacToe.drawBoard(self,self.board)
        playerLetter = 'X'
        AILetter = 'O'
        order = 1
        while True:
            if order == 1:
                if len(ticTacToe.availableMoves(self,self.board))!=0:
                    print('Here are a list of available moves: ', self.availableMoves(self.board))
                    choice = -1
                    while choice not in ticTacToe.availableMoves(self,self.board):
                        selection = input("Please choose a legal move. \n")
                        choice = int(selection)
                    ticTacToe.move(self,self.board, playerLetter, choice)
                    print("result:")
                    ticTacToe.drawBoard(self, self.board)
                    
                    if ticTacToe.checkWin (self, playerLetter, self.board):
                        print(playerLetter, ' won')
                        break
                
                if len(ticTacToe.availableMoves(self,self.board))!=0:
                    aMove = ticTacToe.moveChoice(self,numPlayOut, AILetter, AILetter)
                    ticTacToe.move(self,self.board, AILetter, aMove)
                    print('AI move:', aMove)
                    ticTacToe.drawBoard(self, self.board)
                    
                    if ticTacToe.checkWin (self,AILetter, self.board):
                        print(AILetter, ' won')
                        break
                else:
                    print('No one won')
                    break             
                
                
        # while True:        
            # playerA move
            # aMove = random.choice(self.availableMoves(board))
            # aMove = self.moveChoice(numPlayOut, 'X', 'X')
            # print('aMove:', aMove)
            # print(board)
            # self.move(self.board, 'X', aMove)
            # self.drawBoard(self.board)
            
            # if self.checkWin ('X', self.board):
            #     print('X won')
            #     break
            
            # if len(self.availableMoves(self.board))==0:
            #     print('No one won')
            #     break
            
            # # playerB move
            # aMove = self.moveChoice(numPlayOut, 'O', 'O')
            # # aMove = random.choice(self.availableMoves(board))
            # print('aMove:', aMove)
            # self.move(self.board, 'O', aMove)
            # self.drawBoard(self.board)
            
            # if self.checkWin ('O', self.board):
            #     print ('O won')
            #     break
            
            # if len(self.availableMoves(self.board))==0:
            #     print('No one won')
            #     break
            
    def moveChoice (self, numPlayOut, XorO, AILetter):
        toBeSearchedList = ticTacToe.availableMoves(self, self.board)
        playOutResults = {}
        
        for i in range (numPlayOut):
            if len(toBeSearchedList) > 0:
                aBoard = copy.deepcopy(self.board)
                aMove = random.choice(toBeSearchedList)
                toBeSearchedList.remove(aMove)
                newScore = 0
                newScore = ticTacToe.randomPlayOut(self, numPlayOut, aBoard, aMove, XorO, AILetter, 0, 0)
                if newScore == None:
                    newScore = 0
                playOutResults[newScore] = aMove
        # print(playOutResults)
        bestScore = max(playOutResults.keys())
        bestMove = playOutResults[bestScore]
        return bestMove
    
    def randomPlayOut(self, numPlayOut, aBoard, aMove, XorO, AILetter, aScore, count):
        # set next player
        if XorO == 'X':
            nextXorO = 'O'
        else:
            nextXorO = 'X'
        
        # make a move
        ticTacToe.move(self,aBoard,XorO, aMove)
        
        # check win conditions   
        if ticTacToe.checkWin(self,XorO, aBoard):
            if XorO == AILetter:
                aScore+=1
            else:
                aScore-=1
            return aScore
        if len(self.availableMoves(aBoard))==0:
            return aScore
        
        toBeSearchedList = ticTacToe.availableMoves(self,aBoard)     
        
        for i in range(numPlayOut):
            if len(toBeSearchedList)>0:
                newMove = random.choice(toBeSearchedList)
                toBeSearchedList.remove(newMove)        
                copyBoard = copy.deepcopy(aBoard)
                result = ticTacToe.randomPlayOut(self, numPlayOut, copyBoard, newMove, nextXorO, AILetter, aScore, count)
                if result == None:
                    result = 0     
                aScore += result
        return aScore
                
board = [0,1,2,3,4,5,6,7,8]
newGame = ticTacToe(board)
newGame.aGame()