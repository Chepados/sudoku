import numpy as np
from math import ceil
import pprint
from copy import deepcopy

Y = 0
X = 1

board = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]
board = np.array(board)


def posible_numbers(sudoku, pos):

    set_row = set(sudoku[pos[Y]]) - {0}
    set_col = set([row[pos[X]] for row in sudoku]) - {0}

    square = (ceil((pos[Y] + 1) / 3), ceil((pos[X] + 1) / 3))
    square_matrix = sudoku[(square[0] - 1) * 3:square[0]*3,(square[1] - 1) * 3:square[1]*3]

    set_square = set(square_matrix.reshape((1,9))[0]) - {0}

    return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set_square - set_row - set_col

def sudoku_recursivo(sudoku):

    sudoku_copia = deepcopy(sudoku)

    for i in len(board):
        for j in len(board[0]):
            if board[i][j] == 0:
                numbers = posible_numbers(board, (i, j))
                if numbers == set():
                    return False
                else:
                    for number in numbers:
                        sudoku_copia[i][j] = number




sudoku_recursivo(board)