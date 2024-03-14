#Objeto sudoku

import numpy as np
from math import ceil
from copy import deepcopy
from colorama import Fore
from time import time

Y = 0
X = 1

class Sudoku:
    def __init__(self, nombre):

        def load_board(nombre):
            with open(f"tableros/{nombre}", "r") as archivo:
                tablero = archivo.read()
                tablero = eval(tablero)
                return tablero


        self.__tablero = load_board(nombre)
        self.__solved_board = None

    def solve(self):
        def posible_numbers(sudoku, pos):

            sudoku = np.array(sudoku)

            set_row = set(sudoku[pos[Y]]) - {0}
            set_col = set([row[pos[X]] for row in sudoku]) - {0}

            square = (ceil((pos[Y] + 1) / 3), ceil((pos[X] + 1) / 3))
            square_matrix = sudoku[(square[0] - 1) * 3:square[0] * 3, (square[1] - 1) * 3:square[1] * 3]

            set_square = set(square_matrix.reshape((1, 9))[0]) - {0}

            return {1, 2, 3, 4, 5, 6, 7, 8, 9} - set_square - set_row - set_col

        def sudoku_recursivo(sudoku):
            global terminado

            sudoku_copia = deepcopy(sudoku)

            for i in range(len(sudoku_copia)):
                for j in range(len(sudoku_copia[0])):
                    if sudoku_copia[i][j] == 0:
                        numeros = posible_numbers(sudoku_copia, (i, j))
                        if numeros == set():
                            return None
                        else:
                            for numero in numeros:
                                sudoku_copia[i][j] = numero
                                aux = sudoku_recursivo(sudoku_copia)
                                if aux == None:
                                    continue
                                return aux
                            return None

            return sudoku_copia

        self.__solved_board = sudoku_recursivo(self.__tablero)


    def visualizar_solucion(self):

        board_list = [number for row in self.__tablero for number in row]
        solve_list = [number for row in self.__solved_board for number in row]

        i = 0

        with open("template.txt", "r", encoding="UTF-8") as file:
            string = file.read()

        for char in string:
            if char != "0":
                print(Fore.RESET + char, end="")
            else:
                if board_list[i] != 0:
                    print(Fore.RESET + str(board_list[i]), end="")
                else:
                    print(Fore.GREEN + str(solve_list[i]), end="")
                i += 1



def main():

    time_a = time()

    sudoku = Sudoku("tab_1.txt")
    sudoku.solve()

    time_b = time()

    print(time_b - time_a)

    sudoku.visualizar_solucion()


if __name__ == "__main__":
    main()