from cars import ElectricCar

my_byd = ElectricCar('BYD','seal',2025)
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()