''' 
Walidacja i Przekształcenia Operacji na Macierzach
Stwórz system, który przyjmuje operacje na macierzach jako stringi i wykonuje je dynamicznie,
zapewniając jednocześnie walidację poprawności operacji:
• Operacje mogą obejmować dodawanie, mnożenie i transponowanie macierzy.
• System powinien sprawdzać poprawność operacji (zgodność wymiarów) i zwracać wynik w
postaci macierzy.
• Wykorzystaj eval() i exec() do wykonywania operacji na macierzach, a także funkcje
walidacyjne, które sprawdzają poprawność przed wykonaniem.
Wskazówka: Zaimplementuj walidację operacji i użyj funkcji funkcyjnych do przekształceń i obliczeń na
macierzach.
'''
import numpy as np


def add_matrix_validation(matrix1, matrix2):

    code = """
if matrix1.shape != matrix2.shape:
    raise ValueError(f"Nie można wykonywać dodawania macierzy o różnych wymiarach: {matrix1.shape}, {matrix2.shape}")
    """

    exec(code)

def mutiply_matrix_validation(matrix1, matrix2):
    code = """
if matrix1.shape[1] != matrix2.shape[0]:
    raise ValueError(f"Nie można wykonywać dodawania macierzy o różnych wymiarach: {matrix1.shape}, {matrix2.shape}")
"""
    exec(code)



def add_matrix(matrix1, matrix2):

    add_matrix_validation(matrix1, matrix2)


    result = [[0 for _ in subList] for subList in matrix1]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):

            expr = "matrix1[i][j] + matrix2[i][j]"
            result[i][j] = int(eval(expr))
    
    print("\n")
    for r in result:
        print(r)
    

def multiply_matrix(matrix1, matrix2):

    mutiply_matrix_validation(matrix1, matrix2)

    expr = "np.dot(matrix1, matrix2)"
    result = eval(expr)

    print("\n")
    for r in result:
        print(r)

def tranpor_matrix(matrix):

    expr = "matrix.T"
    result = eval(expr)

    print("\n")
    for r in result:
        print(r)

