favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'rust',
    'paweł': 'python',
}  # słownik

friends = ['paweł', 'sara']
for name in favorite_languages.keys():
    print(f"Witaj, {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem programowania jest {language}.")

if 'elzbieta' not in favorite_languages.keys():
    print("Elzbieta, proszę weź udział w naszej ankiecie!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, dziękujemy za udział w ankiecie.")

print("W ankiecie zostały wymienione następujące języki programowania:")
for language in set(favorite_languages.values()):
    print(language.title())

languages = {'c', 'python', 'rust', 'python'}  # zbiór
print(languages)
