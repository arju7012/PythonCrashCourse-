cities = {
    'cochin': {
        'country': 'india',
        'population': 878000,
        'fact': "It's been described as the world's largest electric boat metro transportation infrastructure, and it's a really cool way to get around and see the city from a different perspective.",
    },
    'new york': {
        'country': 'usa',
        'population': 19867248,
        'fact': "It's estimated that over 800 languages are spoken within the five boroughs. That makes it the most linguistically diverse city in the world!",
    },
    'shanghai': {
        'country': 'china',
        'population': 24874500,
        'fact': "Shanghai has the world's largest subway system!.",
    },

}

for city, city_info in cities.items():
    print(f"\n{city.capitalize()}")
    print(f"\t{city.title()} is in {city_info['country']}")
    print(f"\tTheir population is around {city_info['population']}")
    print(f"\tIt is true that {city_info['fact']}")
