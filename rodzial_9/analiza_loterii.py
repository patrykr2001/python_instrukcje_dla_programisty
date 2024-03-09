from loteria import Loteria

my_loteria = Loteria()
winning_ticket = my_loteria.losuj_znaki()
my_ticket = my_loteria.losuj_znaki()
liczba_iteracji = 0

while my_ticket != winning_ticket:
    liczba_iteracji += 1
    my_ticket = my_loteria.losuj_znaki()

print(liczba_iteracji)
