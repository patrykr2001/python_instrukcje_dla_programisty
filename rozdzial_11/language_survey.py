from survey import AnonymousSurvey

# Zdefiniowanie pytania i utworzenie ankiety
question = "Jaki jest Twój ojczysty język?"
language_survey = AnonymousSurvey(question)

# Wyświetla pytania i przechowanie odpowiedzi na nie
language_survey.show_question()
print("Wpisz 'q', aby zakończyć działanie programu.")
while True:
    response = input("Język: ")
    if response == "q":
        break
    language_survey.store_response(response)

# Wyświetlanie wyników ankiety
print("\nDziękujemy każdemu respondentowi za udział w ankiecie!")
language_survey.show_results()
