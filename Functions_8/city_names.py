def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'

feroke_city = city_country("feroke", "india")
print(feroke_city)
texas_city = city_country("texas", "united states of america")
print(texas_city)

