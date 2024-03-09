from random import randint


class Loteria:
    def __init__(self):
        self.znaki = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

    def losuj_znaki(self):
        wylosowane = []
        for i in range(4):
            los = randint(0, len(self.znaki) - 1)
            wylosowane.append(self.znaki[los])

        return wylosowane
