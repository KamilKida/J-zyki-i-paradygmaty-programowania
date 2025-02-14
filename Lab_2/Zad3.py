'''
Dynamiczne Wyznaczanie Ekstremów w Niejednorodnych Danych
Napisz funkcję, która przyjmuje listę niejednorodnych danych (np. liczby, napisy, krotki, listy, słowniki) i
wykonuje dynamiczną analizę danych, aby:
• Zwrócić największą liczbę (lub wartość numeryczną) w danych.
• Zwrócić najdłuższy napis.
• Zwrócić krotkę o największej liczbie elementów.
Wskazówka: Użyj filter() do selekcji odpowiednich typów danych oraz map() do przekształceń na
elementach.
'''

def dinamic_extremes_determination(list_of_extremes):
    # list_of_numbers = list(filter(lambda x: type(x) in (int, float), list_of_extremes))
    # list_of_words = list(filter(lambda x: type(x) in str, list_of_extremes))
    # list_of_tuple = list(filter()lambda x: type(x) in tuple, list_of_extremes))

    max_number = max(list(filter(lambda x: type(x) in (int, float), list_of_extremes)))
    longest_word = max(list(filter(lambda x: isinstance(x, str), list_of_extremes)), key=len)
    longest_tuple = max(list(filter(lambda x: isinstance(x, tuple), list_of_extremes)), key= len)

    print(f"Największy numer: {max_number}")
    print(f"Najdłuższe słowo: {longest_word}")
    print(f"Najdłuższa krotka: {longest_tuple}")