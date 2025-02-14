'''
    Zadanie 3 Optymalizacja Rozmieszczenia Zadań (Proceduralne i Funkcyjne)
Masz N zadań do wykonania, każde zadanie ma przypisany czas wykonania oraz nagrodę za jego
ukończenie. Twoim celem jest zaplanowanie kolejności wykonywania zadań, aby zminimalizować
całkowity czas oczekiwania na ich wykonanie i zmaksymalizować zysk. Zaimplementuj rozwiązanie przy
użyciu programowania proceduralnego oraz funkcyjnego.
Wymagania:
• Proceduralnie: Stwórz listę zadań i użyj pętli do sortowania i optymalizacji ich kolejności, aby
zminimalizować całkowity czas oczekiwania.
• Funkcyjnie: Użyj funkcji wyższego rzędu (sorted, map, reduce) do manipulacji listą zadań, aby
osiągnąć optymalne rozwiązanie.
• Program powinien zwrócić optymalną kolejność zadań oraz całkowity czas oczekiwania.
    '''

# wersja proceduralna
def optimizeTaskProcedure(tasks):
    # sortowanie zadan malejaco wedlug wartosci nagroda/czas
    tasks.sort(key = lambda x: -x['reward'] / x['time'])
    total_reward = 0
    total_time = 0
    task_order = []

    for task in tasks:
      task_order.append(task)
      total_time += task['time']
      total_reward += task['reward']

    return total_reward, task_order



#wersja funkcjna
def optimizeTaskFunction(tasks):
    # sortowanie zadan malejaco wedlug wartosci nagroda/czas
    key_func = lambda task: -task['reward'] / task['time']
    sorted_task = sorted(tasks, key = key_func)

    total_reward = sum(map(lambda task : task['reward'], sorted_task))

    return total_reward, sorted_task
