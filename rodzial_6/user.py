user_0 = {
    'username': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski',
}

for key, value in user_0.items():
    print(f"\nKlucz: {key}")
    print(f"Wartość: {value}")

for key in user_0.keys():
    print(f"\nKlucz: {key}")

for value in user_0.values():
    print(f"\nWartość: {value}")
