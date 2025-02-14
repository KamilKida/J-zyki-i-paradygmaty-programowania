'''
Problem Optymalizacji Zasobów – Algorytm Plecakowy (Proceduralne i Funkcyjne)
Masz ograniczoną pojemność plecaka oraz listę przedmiotów, z których każdy ma określoną wagę i
wartość. Celem jest wybranie przedmiotów tak, aby zmaksymalizować łączną wartość w plecaku, nie
przekraczając jego pojemności. Problem ten wymaga implementacji algorytmu plecakowego (knapsack
problem) przy użyciu zarówno podejścia proceduralnego, jak i funkcyjnego.
Wymagania:
• Proceduralnie: Użyj podejścia dynamicznego (programowanie dynamiczne) do rozwiązania
problemu.
• Funkcyjnie: Zaimplementuj algorytm w stylu funkcyjnym z naciskiem na funkcje rekurencyjne
oraz mapowanie.
• Program powinien zwracać maksymalną wartość oraz listę przedmiotów, które powinny zostać
wybrane do plecaka.
'''


from functools import lru_cache

#wersja proceduralna
def sortBackPackProcedure(items, capacity):

    bag = [0] * (capacity + 1)
    item_selection = [[] for _ in range(capacity + 1)]

    for name, value, weight in items:
        for i in range(capacity, weight - 1, -1):
            if bag[i] < bag[i - weight] + value:
                bag[i] = bag[i - weight] + value
                item_selection[i] = item_selection[i - weight] + [(name, value, weight)]

    return round(bag[capacity]), item_selection[capacity]

#wersja funkcyjna
def sortBackPackFunction(items, capacity):
    @lru_cache(None)

    def solve(index, remaining_capacity):
        if index == len(items) or remaining_capacity == 0:
            return 0,[]
        
        name, value, weight = items[index]

        without_item_value, without_item_list = solve(index + 1, remaining_capacity)

        if weight <= remaining_capacity:
            with_item_value, with_item_list = solve(index + 1, remaining_capacity - weight)
            with_item_value += value

            if with_item_value > without_item_value:
                return with_item_value, [(name, value, weight)] + with_item_list

        return without_item_value, without_item_list

    return solve(0, capacity)