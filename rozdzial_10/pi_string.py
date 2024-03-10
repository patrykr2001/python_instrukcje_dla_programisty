from pathlib import Path

path = Path('pliki_danych/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Podaj datę urodzenia: ")
if birthday in pi_string:
    print("Twoja data znajduje się w pierwszym milionie liczby pi!")
else:
    print("Twoja data nie znajduję się w pierwszym milionie liczby pi!")
