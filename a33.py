import random   
import copy
import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(500000)
# draws out physical representation of game

class ticTacToe:
    def __init__(self, board):
        self.board = board
        
    def drawBoard(self, board):
        print(board[6], ' | ', board[7], ' | ' , board [8])
        print('_____________')
        print(board[3] , ' | ' , board[4] , ' | ' , board [5])
        print('_____________')
        print(board[0] , ' | ' , board[1] , ' | ' , board [2])
        print()
        print()

    # gets player input on choice of letter
    # def playerChoice(self):
    #     letter = ''
    #     while not (letter == 'X' or letter == 'O'):
    #         print('Do you want to be X or O?')
    #         letter = input().upper()
            
    #         if letter == 'X':
    #             return ['X', 'O']
    #         else:
    #             return ['O', 'X']
            
    # # decides who goes first through random selection
    # def whoGoesFirst(self):
    #     if random.randint(0,1) == 0:
    #         return 'AI'
    #     else:
    #         return 'player'

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

    def aGame(self):
        count = 0
        numPlayOut = 10
        while True:
            # playerA move
            # aMove = random.choice(self.availableMoves(board))
            aMove = self.moveChoice(numPlayOut, 'X', 'X')
            print('aMove:', aMove)
            print(board)
            self.move(self.board, 'X', aMove)
            self.drawBoard(self.board)
            count+=1
            print("count: ", count)
            
            if self.checkWin ('X', self.board):
                print('X won')
                break
            
            if len(self.availableMoves(self.board))==0:
                print('No one won')
                break
            
            # playerB move
            aMove = self.moveChoice(numPlayOut, 'O', 'O')
            # aMove = random.choice(self.availableMoves(board))
            print('aMove:', aMove)
            self.move(self.board, 'O', aMove)
            self.drawBoard(self.board)
            count+=1
            print("count: ", count)
            
            if self.checkWin ('O', self.board):
                print ('O won')
                break
            
            if len(self.availableMoves(self.board))==0:
                print('No one won')
                break
            
    def moveChoice (self, numPlayOut, XorO, AILetter):
        if XorO == 'X':
            nextXorO = 'O'
        else:
            nextXorO = 'X'
        
        toBeSearchedList = ticTacToe.availableMoves(self, self.board)
        playOutResults = {}
        
        for i in range (numPlayOut):
            if len(toBeSearchedList) > 0:
                aBoard = copy.deepcopy(self.board)
                aMove = random.choice(toBeSearchedList)
                toBeSearchedList.remove(aMove)
                ticTacToe.move(self,aBoard,XorO,aMove) 
                newScore = ticTacToe.randomPlayOut(self, numPlayOut, aBoard, nextXorO, AILetter, 0, 0)
                
                if newScore == None:
                    newScore = 0
                # print('newScore: ', newScore)
                
                playOutResults[aMove] = newScore
        print(playOutResults)
        bestMove = max(playOutResults.keys())
        max_key = max(playOutResults, key=playOutResults.get)
        return max_key
    
    def randomPlayOut(self, numPlayOut, aBoard, XorO, AILetter, aScore, count):
        count+=1
        # print('recursion count:', count)
        
        # set next player
        if XorO == 'X':
            nextXorO = 'O'
        else:
            nextXorO = 'X'
            
        # check win condition   
        if self.checkWin('X', aBoard):
            if 'X' == AILetter:
                aScore+=1
            else:
                aScore-=1
            return aScore
        if self.checkWin('O', aBoard):
            if 'O' ==AILetter:
                aScore+=1
            else:
                aScore-=1
            return aScore
        if len(self.availableMoves(aBoard))==0:
            return aScore
        
        toBeSearchedList = ticTacToe.availableMoves(self,aBoard)     
        
        for i in range(numPlayOut):
   
            if len(toBeSearchedList)>0:
                aMove = random.choice(toBeSearchedList)
                toBeSearchedList.remove(aMove)        
                copyBoard = copy.deepcopy(aBoard)
                ticTacToe.move(self,copyBoard,XorO,aMove)
                # ticTacToe.drawBoard(self, aBoard)
                ticTacToe.randomPlayOut(self, numPlayOut, copyBoard, nextXorO, AILetter, aScore, count)
        
board = [0,1,2,3,4,5,6,7,8]
newGame = ticTacToe(board)
newGame.aGame()