def greet_users(names):
    """Wyświetla proste powitanie każdemu użytkownika z listy."""
    for name in names:
        msg = f"Witaj, {name.title()}!"
        print(msg)


usernames = ['halina', 'tymek', 'marzec']
greet_users(usernames)
