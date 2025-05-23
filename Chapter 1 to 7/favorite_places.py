favorite_places = {
    'arjun': ["new zealand", "africa", "greenland"],
    'babi': ["antartica", "narikuni", "eravannur"],
    'sharath': ["manali", "new york", "japan"],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")