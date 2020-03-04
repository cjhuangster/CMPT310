import random  

def drawBoard(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board [9])
    print('_____________')
    print(board[4] + ' | ' + board[5] + ' | ' + board [6])
    print('_____________')
    print(board[1] + ' | ' + board[2] + ' | ' + board [3])
    print('_____________')
    
def playerChoice():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
        
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'AI'
    else:
        return 'player'

def move (board, letter, move):
    board[move] = letter
    
def checkWin (XorO, board):
    return ((board[1]==board[2]==board[3]==XorO) 
    or (board[4]==board[5]==board[6]==XorO)
    or (board[7]==board[8]==board[9]==XorO)
    or (board[1]==board[4]==board[7]==XorO)
    or (board[2]==board[5]==board[8]==XorO)
    or (board[3]==board[6]==board[9]==XorO)
    or (board[1]==board[5]==board[9]==XorO)
    or (board[3]==board[5]==board[7]==XorO))
    
def availableMoves (board):
    availableSpace = []
    for i in board:
        if board[i] == '':
            availableSpace.append(i)
    return availableSpace

