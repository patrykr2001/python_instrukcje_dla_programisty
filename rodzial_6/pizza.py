pizza = {
    'crust': 'grubym',
    'toppings': ['pieczarki', 'podwójny ser'],
}

print(f"Zamówiłeś pizzę na {pizza['crust']} cieście wraz z następującymi dodatkami:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

