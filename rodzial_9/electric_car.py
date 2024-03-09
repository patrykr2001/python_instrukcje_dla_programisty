"""Zestaw klas potrzebnych do zaprezentowania samochodu elektrycznego."""

from car import Car


class Battery:
    """Proste modelowanie baterii samochodu."""

    def __init__(self):
        self.battery_size = 40

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.")

    def get_range(self):
        """Wyświetla informację o zasięgu samochodu na podstawię akumulatora."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"Zasięg tego samochodu wynosi {range} km po pełnym naładowaniu akumulatora.")


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """
        Inicjacja atrybutów klasy nadrzędnej.
        Następnie inicjalizacja atrybutów charakterystycznych dla samochodu elektrycznego.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
