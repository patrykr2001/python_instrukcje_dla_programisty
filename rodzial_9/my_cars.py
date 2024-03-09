from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = ElectricCar('tesla', '3', 2023)
print(my_tesla.get_descriptive_name())
