from pathlib import Path

path = Path("./pliki_danych/alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Przepraszamy, ale plik {path} nie istnieje.")
else:
    # Obliczanie przybliżonej liczby słów w pliku.
    words = contents.split()
    num_words = len(words)
    print(f"Plik {path} zawiera {num_words} słów.")
