number = input("Podaj liczbę, aby dowiedzieć się, czy jest parzysta czy nieparzysta: ")
number = int(number)

if number % 2 == 0:
    print(f"Liczba {number} jest parzysta.")
else:
    print(f"Liczba {number} jest nieparzysta.")
