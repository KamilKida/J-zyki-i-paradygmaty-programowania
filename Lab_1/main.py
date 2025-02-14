from Zad1 import podziel_paczki
from Zad2 import bfs_shortest_path
from Zad3 import optimizeTaskFunction
from Zad3 import optimizeTaskProcedure
from Zad4 import sortBackPackProcedure
from Zad4 import sortBackPackFunction
from Zad5 import tasksOrginizeProcedure
from Zad5 import tasksOrginizeFunctional

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #zad1
    # wagi = [10, 15, 7, 20, 5, 8, 10]
    # max_waga = 25

    # liczba_kursow, kursy = podziel_paczki(wagi, max_waga)

    # print(f"Liczba kurów: {liczba_kursow}")
    # for i, kurs in enumerate(kursy, 1):
    #     print(f"Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg.")

    
    # # zad2.
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['A', 'D', 'E'],
    #     'C': ['A', 'F'],
    #     'D': ['A'],
    #     'E': ['B', 'F'],
    #     'F': ['C', 'E']
    # }
    # print(bfs_shortest_path(graph,'A', 'F'))
    

    # #zad3
    # task = [
    # {'time' : 3, 'reward': 10},
    # {'time' : 2, 'reward': 5},
    # {'time' : 1, 'reward': 8},
    # {'time' : 4, 'reward': 7}
    #         ]


    # print(optimizeTaskFunction((task)))
    # print(optimizeTaskProcedure((task)))
    
    #zad4
    # items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]
    # capacity = 50
    # print(sortBackPackProcedure(items, capacity))

    # items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]
    # capacity = 50
    # print(sortBackPackFunction(tuple(items), capacity))

    #zad5
    tasks = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (7, 8, 3), (6, 9, 9)]
    print(tasksOrginizeProcedure(tasks))
    print(tasksOrginizeFunctional(tasks))