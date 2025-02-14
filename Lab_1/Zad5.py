'''
Harmonogramowanie Zadań z Ograniczeniami (Programowanie Funkcyjne i Proceduralne)
Masz zestaw zadań, gdzie każde zadanie ma określony czas rozpoczęcia, zakończenia oraz nagrodę za
ukończenie. Twoim celem jest opracowanie harmonogramu, który maksymalizuje nagrodę, wykonując
jak najwięcej niekolidujących zadań. Zadanie wymaga implementacji algorytmu planowania zadań,
podobnego do problemu aktywności (Activity Selection Problem) przy użyciu podejścia proceduralnego
i funkcyjnego.
Wymagania:
• Proceduralnie: Zaimplementuj algorytm zachłanny do selekcji zadań na podstawie czasu
zakończenia.
• Funkcyjnie: Wykorzystaj funkcje wyższego rzędu, takie jak filter, sorted, reduce, aby
przefiltrować i posortować zadania oraz wybrać optymalny harmonogram.
• Program powinien zwracać maksymalną możliwą nagrodę i listę zadań w optymalnym
harmonogramie.
'''
from functools import reduce

#wersja proceduralna
def tasksOrginizeProcedure(tasks):

    tasks_sorted = sorted(tasks, key=lambda x: x[1])

    selected_tasks = []
    total_reward = 0

    last_end_time = 0

    for start, end, reward in tasks_sorted:
        if start >= last_end_time:
            selected_tasks.append((start, end, reward))
            total_reward += reward
            last_end_time = end

    return total_reward, selected_tasks

#wersja funkcyjna
def tasksOrginizeFunctional(tasks):
     
    tasks_sorted = sorted(tasks, key=lambda x: x[1])

    def canScheduleFunction(selected, task):
        if selected and selected[-1][1]:
            return selected + [task]
        elif not selected:
            return [task]
        return selected
    

    selected_tasks = reduce(canScheduleFunction, tasks_sorted, [])

    total_reward = sum(reward for _, _, reward in selected_tasks)

    return total_reward, selected_tasks