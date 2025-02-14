'''
Zadanie 2. Wyznaczanie Najkrótszej Ścieżki (Programowanie Funkcyjne)
Stwórz program obliczający najkrótszą ścieżkę w grafie nieważonym przy użyciu algorytmu BFS
(Breadth-First Search). Implementacja powinna być zrealizowana przy użyciu programowania
funkcyjnego z naciskiem na niemutowalne struktury danych, funkcje lambda, i mapowanie.
Wymagania:
• Napisz funkcję BFS przy użyciu funkcyjnego podejścia z rekurencją lub funkcjami wyższego
rzędu.
• Zaimplementuj graf jako słownik (dict), gdzie klucz to wierzchołek, a wartość to lista sąsiednich
wierzchołków.
• Funkcja powinna przyjmować graf oraz wierzchołek początkowy i końcowy, zwracając
najkrótszą ścieżkę jako listę wierzchołków.
'''

from collections import deque
from turtledemo.penrose import start

def bfs_shortest_path(graph, start, end):

    queue = deque([[start]]) # struktura do przechowwania sciezki

    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path

        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

        return None