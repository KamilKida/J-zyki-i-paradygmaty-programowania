'''
Zadanie 1. Analiza Tekstu i Transformacje Funkcyjne
Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji
analizy tekstu:
• Zlicza liczbę słów, zdań, i akapitów w tekście.
• Wyszukuje najczęściej występujące słowa, wykluczając tzw. stop words (np. "i", "a", "the").
• Transformuje wszystkie wyrazy rozpoczynające się na literę "a" lub "A" do ich odwrotności (np.
"apple" → "elppa").
'''
from collections import Counter


def analizeText(text):
    paragraphs= text.split('\n')
    sentences = [sentence for paragraph in paragraphs for sentence in paragraph.split('.')]
    words = text.split(" ")

    print(f"Liczba akapitów: {len(paragraphs)}")
    print(f"Liczba zdań: {len(sentences)}")
    print(f"Liczba znaków: {len(words)}")


    stop_words = {'a', 'z', 'i', 'o', 'the', 'or', 'to'}
    filtered_words = filter(lambda word: word not in stop_words, words)
    word_counter = Counter(filtered_words)
    most_common = word_counter.most_common(5)

    print(f"Najczęstrze słowa: {most_common}")

    reversAWords = [word[::-1] if word.lower().startswith('a') else word for word in words]
    print((f"Odwrócone słowa rozpoczynajace sie na 'a': {' '.join(reversAWords)}"))
