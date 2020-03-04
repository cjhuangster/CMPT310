import random   

# draws out physical representation of game
class ticTacToe:
    def __init__(self):
        self.board = ['X',1,2,3,4,5,6,7,8,9]
        
    def drawBoard(self, board):
        print()
        print()
        print(board[7], ' | ', board[8], ' | ' , board [9])
        print('_____________')
        print(board[4] , ' | ' , board[5] , ' | ' , board [6])
        print('_____________')
        print(board[1] , ' | ' , board[2] , ' | ' , board [3])

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
        return ((board[1]==board[2]==board[3]==XorO) 
        or (board[4]==board[5]==board[6]==XorO)
        or (board[7]==board[8]==board[9]==XorO)
        or (board[1]==board[4]==board[7]==XorO)
        or (board[2]==board[5]==board[8]==XorO)
        or (board[3]==board[6]==board[9]==XorO)
        or (board[1]==board[5]==board[9]==XorO)
        or (board[3]==board[5]==board[7]==XorO))
        
    # returns a list of available moves
    def availableMoves (self, board):
        availableSpace = []
        print("board: ", board)
        for i in board:
            # bugged, returning positions that have already been filled
            if i != 'X' and i != 'O':
                availableSpace.append(i)
        
        print("availableSpace: ", availableSpace)
        return availableSpace

    def aGame(self):
        board = ['X',1,2,3,4,5,6,7,8,9]
        count = 0
        while True:
                aMove = random.choice(self.availableMoves(board))
                # print(aMove)
                self.move(board, 'X', aMove)
                self.drawBoard(board)
                count+=1
                print("count: ", count)
                if self.checkWin ('X', board):
                    print('X won')
                    break
                
                if len(self.availableMoves(board))==0:
                    print('No one won')
                    break
                
                aMove = random.choice(self.availableMoves(board))
                self.move(board, 'O', aMove)
                self.drawBoard(board)
                count+=1
                print("count: ", count)
                
                if self.checkWin ('O', board):
                    print ('O won')
                
                if len(self.availableMoves(board))==0:
                    print('No one won')
                    break
# recursively playout game
class pMCTS:
    def __init__(self, XorO, move, numPlayOut):
        self.numPlayOut = numPlayOut
        self.numWins = []
    
    def randomPlayOut(self, numPlayOut, copyAvailableMoves, board, XorO, AILetter, playerLetter, score):
        playOut = ticTacToe(board)
        nextXorO = ''
        if XorO == 'X':
            nextXorO == 'O'
        else:
            nextXorO == 'X'
        # check win condition
        if playOut.checkWin (playerLetter, board):
            score-=1
            return score
        if playOut.checkWin (AILetter, board):
            score+=1
            return score
        if len(playOut.availableMoves(board))==0:
            return score
        
        for i in range(numPlayOut):
            # how to avoid passing by reference of OG availableMoves?
            # deep copy a copy of available, pop the move made in current iteration, pass to next
            aMove = random.choice(playOut.copyAvailableMove)

            score += randomPlayOut(numPlayOut, board, nextXorO, AILetter, playerLetter)
              
newGame = ticTacToe()
newGame.aGame()