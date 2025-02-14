'''
Implementacja Złożonej Funkcji Matrycowej z Użyciem reduce()
Napisz program, który przyjmuje listę macierzy i łączy je w jedną za pomocą operacji zdefiniowanej
przez użytkownika (np. suma macierzy, iloczyn), korzystając z reduce(). Program powinien:
• Dynamicznie wywoływać różne operacje (np. sumowanie, mnożenie) na macierzach.
• Umożliwiać definiowanie niestandardowych operacji przez użytkownika.
Wskazówka: Wykorzystaj reduce() do łączenia macierzy oraz eval() do dynamicznej definicji operacji.
'''

import numpy as np
from functools import reduce

def dynamic_matrix_operations(matrices_list, operation):

    if operation not in dir(np):
        raise ValueError(f"Operacja '{operation}' nie jest zdefiniowana w module numpy.")
    
    op_function = getattr(np, operation)

    result = reduce(op_function, matrices_list)
    
    for r in result:
        print(r)