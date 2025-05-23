favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
friends = ['phil', 'sarah', 'arjun']

for name in favorite_language.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}")

for name in sorted(favorite_language.keys()):
    print(f"{name.title()},thank you for taking the poll.")

for name in friends:
    if name not in favorite_language.keys():
        print(f"{name}, please take the poll.")