def make_car(manufacture, model_name, **car_info):
    car_info['manufacture'] = manufacture
    car_info['model_name'] = model_name
    return car_info
car = make_car('ferrari', 'blalba', color = 'red')
print(car)