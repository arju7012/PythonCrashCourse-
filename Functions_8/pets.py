def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'pablo')
describe_pet(pet_name='buddy', animal_type='cat')