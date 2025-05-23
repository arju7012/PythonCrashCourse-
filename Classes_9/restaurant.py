class Restaurant:
    """A simple class for understanding the restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {self.cuisine_type} type restaurant. This restaurant has served {self.number_served} people.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open now!!")

    def set_number_served(self, num):
        if num >= self.number_served:
            self.number_served = num

    def increment_number_served(self, people):
        self.number_served += people

        

restaurant = Restaurant('Paragon', 'Indian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(15)
restaurant.describe_restaurant()
restaurant.increment_number_served(5)
restaurant.describe_restaurant()


"""restaurant_2 = Restaurant('Majilis', 'Arabian')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('WoW Momos', 'Chineese')
restaurant_3.describe_restaurant()
restaurant_4 = Restaurant('Thossai', 'Indian veg')
restaurant_4.describe_restaurant()"""