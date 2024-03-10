class AnonymousSurvey:
    """Przechowuje anonimowe odpowiedzi na pytania w ankiecie."""

    def __init__(self, question):
        """Przechowuje pytanie i przygotowuje odpowiedzi."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Wyświetla pytanie ankiety."""
        print(self.question)

    def store_response(self, response):
        """Przechowuje pojedyńczą odpowiedź na pytanie."""
        self.responses.append(response)

    def show_results(self):
        """Wyświetla wszystkie udzielone odpowiedzi."""
        print("Oto wynik ankiety:")
        for response in self.responses:
            print(f"- {response}")
