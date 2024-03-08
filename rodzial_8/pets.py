def describe_pet(pet_name, animal_type='pies'):
    """Wyświetla informację o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")


describe_pet('harry', 'chomik')
describe_pet(pet_name='willie')
describe_pet(animal_type='chomik', pet_name='harry')
