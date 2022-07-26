import random
import colorama
import numpy as np
colorama.init(autoreset=True)
n = random.randrange(3, 11, 1)
def create_board(n):
    board = []
    for i in range(0, n-1):
        board.append(random.randrange(0, n-1, 1))
    print(n-1)
    print(board)
    return board
    #board = np.zeros((n-1,n-1))
    #print(board)

def show_visuall_board(n,board):
    visuall_board = np.ones((n-1,n-1), dtype=str)
    for i in range(len(board)):
        queen_loc = (board[i], i )
        visuall_board[queen_loc] = 'Q'

    print(visuall_board)

def threats(board):
    rand = random.randrange(1,n-1)
    count = 0
    for i in range(len(board)-1):
        for j in range(i+1,len(board)):
            if board[i] == board[j]:
                count += 1
            elif board[i] == board[j] + j - i or board[i] == board[j] + i -j:
                print(str(i) + 'i')
                print(str(j) + 'j')
                count += 1
    print(count)
    return count
board = create_board(n)
show_visuall_board(n,board)
threats(board)