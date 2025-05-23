def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    for model in completed_models:
        print(model.title())