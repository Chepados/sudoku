from Sudoku import Sudoku
import os

lista_sudokus = os.listdir("tableros")

finalizado = False
while not finalizado:

    entrada = input("\n(A)Buscar un sudoku concreto.\n(B)Ver opciones y seleccionar.\n(C)Salir.\n\n")

    if entrada.upper() == "A":
        sudoku_name = input("Escribe el nombre del sudoku que deseas cargar: ")
        if sudoku_name in lista_sudokus:
            sudoku = Sudoku(sudoku_name)
    elif entrada.upper() == "B":
        for i, sudoku_name in enumerate(lista_sudokus):
            print(f"({i}) {sudoku_name}")

        indice_sudoku = int(input("\nEscribe tu seleccion: "))

        if indice_sudoku in range(len(lista_sudokus)):
            sudoku = Sudoku(lista_sudokus[indice_sudoku])
    else:
        finaliado = True


    print("Visualizacion de la solucion:\n")

    sudoku.solve()
    sudoku.visualizar_solucion()