from collections import deque
from turtledemo.penrose import start

'''
Zadanie 1. Problem Podziału Paczek (Programowanie Proceduralne)
Mamy listę paczek o różnych wagach oraz maksymalną wagę, jaką może unieść kurier w jednym kursie.
Twoim zadaniem jest podzielić paczki na jak najmniejszą liczbę kursów, aby każda waga nie przekraczała
maksymalnej dozwolonej wagi. Program powinien korzystać z algorytmu zachłannego do optymalizacji
podziału paczek.
Wymagania:
• Napisz funkcję, która przyjmuje listę wag paczek i maksymalną wagę.
• Użyj pętli for i instrukcji warunkowych if, else do iteracyjnego podziału paczek.
• Program powinien zwracać minimalną liczbę kursów oraz listę paczek w każdym kursie.
'''

def podziel_paczki(wagi,max_waga):
    #sortowanie paczki
    wagi_sort = sorted(wagi,reverse = True)
    kursy = []

    #sprawdzanie czy paczka nie przekracza wartosci max
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza dozwolona wage kursu ({max_waga} kg.)")

    # iteracja po dostepnych paczkach
    for waga in wagi_sort:
        dodano = False
        # szukanie kursu do ktorego mozna dodac paczke
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        # jesli nie mozna dodac paczki do zadnego kursu utworz any kurs
        if not  dodano:
            kursy.append([waga])

    return  len(kursy), kursy
