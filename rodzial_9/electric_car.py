from car import Car


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """
        Inicjacja atrybutów klasy nadrzędnej.
        Następnie inicjalizacja atrybutów charakterystycznych dla samochodu elektrycznego.
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora."""
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
