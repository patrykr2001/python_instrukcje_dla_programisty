def get_formatted_name(first, last, middle=''):
    """Generuje elegancko sformatowane imię i nazwisko."""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()
