def print_models(unprinted_designs, completed_models):
    """
    Symulujemy wydruk poszczególnych projektów, dopóki pozostał jakikolwiek projekt na liście. Każdy wydrukowany model
    zostaje przeniesiony na listę completed_models.
    :param unprinted_designs: Lista projektów do wydrukowania.
    :param completed_models: Lista wydrukowanych modeli.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    Wyświetla wszystkie modele, które zostały wydrukowane.
    :param completed_models: Lista wydrukowanych modeli.
    """
    print("\nWydrukowane zostały następujące modele:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
