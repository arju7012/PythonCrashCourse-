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


class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("We have the following flavors available.")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
        

club_ice = IceCreamStand("Club Ice")
club_ice.flavors = ["fig", "mango", "grape", "watermelon"]

club_ice.set_number_served(15)
club_ice.describe_restaurant()
club_ice.show_flavors()


