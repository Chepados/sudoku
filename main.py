#Codigo codewars

import numpy as np
from math import ceil
from copy import deepcopy

Y = 0
X = 1


def posible_numbers(sudoku, pos):

    sudoku = np.array(sudoku)

    set_row = set(sudoku[pos[Y]]) - {0}
    set_col = set([row[pos[X]] for row in sudoku]) - {0}

    square = (ceil((pos[Y] + 1) / 3), ceil((pos[X] + 1) / 3))
    square_matrix = sudoku[(square[0] - 1) * 3:square[0]*3,(square[1] - 1) * 3:square[1]*3]

    set_square = set(square_matrix.reshape((1,9))[0]) - {0}

    return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set_square - set_row - set_col

def sudoku(my_sudoku):

    sudoku_copia = deepcopy(my_sudoku)

    for i in range(len(sudoku_copia)):
        for j in range(len(sudoku_copia[0])):
            if sudoku_copia[i][j] == 0:
                numeros = posible_numbers(sudoku_copia, (i, j))
                if numeros == set():
                    return None
                else:
                    for numero in numeros:
                        sudoku_copia[i][j] = numero
                        aux = sudoku(sudoku_copia)
                        if aux == None:
                            continue
                        return aux
                    return None

    return sudoku_copia