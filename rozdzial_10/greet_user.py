from pathlib import Path
import json


def get_stored_username(path):
    """Pobranie imienia z pliku, o ile taki istnieje."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Poproszenie użytkownika o podanie imienia, a następnie zapisanie w pliku."""
    username = input("Jak masz na imię? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Witamy ponownie, {username}!")
    else:
        username = get_new_username(path)
        print(f"Twoje imię zostało zapisane i będzie używane później, {username}!")





greet_user()
