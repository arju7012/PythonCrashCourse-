class Car:
    """A simple attempt to represent a car."""


    def __init__(self,make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Print statement showing the car's mileage"""
        print(f"This cas has {self.odometer_reading} kms on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back to the odometer!")

    def increment_odometer(self,kms):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += kms

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self,make,model,year):
        """Initilize attributes of the parent class."""
        super().__init__(make,model,year)
        


my_tiago = ElectricCar('tata','tiago',2024)
print(my_tiago.get_descriptive_name())
