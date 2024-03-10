from pathlib import Path


def count_words(path):
    """Obliczanie przybliżonej liczby słów w danym pliku."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # print(f"Przepraszamy, ale plik {path} nie istnieje.")
        pass
    else:
        # Obliczanie przybliżonej liczby słów w pliku.
        words = contents.split()
        num_words = len(words)
        print(f"Plik {path} zawiera {num_words} słów.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path('./pliki_danych/' + filename)
    count_words(path)
