from datetime import datetime
import random


class Car:
    def __init__(
            self,
            fuel_consumption: float,
            manufacturer: str,
            model: str,
            car_year: int = 2020):

        self.car_year = car_year
        self.manufacturer = manufacturer
        self.total_odo = 0
        self.model = model
        self.fuel_consumption = fuel_consumption

    def __del__(self):
        with open('cars.csv', mode='a', encoding='utf-8') as cars:
            cars.write(f"{self.manufacturer};{self.model};{self.car_year};{datetime.now().date()}\n")


class CargoCar(Car):
    def __init__(self, fuel_consumption: float, manufacturer: str, model: str, car_year: int, lifting_capacity: int):
        super().__init__(fuel_consumption, manufacturer, model, car_year)
        self.lifting_capacity = lifting_capacity

    def __str__(self):
        return f"Manufacturer: {self.manufacturer} \n" \
               f"Model: {self.model} \n" \
               f"Fuel consumption: {self.fuel_consumption} \n" \
               f"Car year: {self.car_year}\n" \
               f"Lifting capacity: {self.lifting_capacity}\n"


class SportCar(Car):
    def __init__(self, fuel_consumption: float, manufacturer: str, model: str, price: int, car_year: int, max_speed: int):
        super().__init__(fuel_consumption, manufacturer, model, car_year)
        self.price = price
        self.max_speed = max_speed

    def __str__(self):
        return f"Manufacturer: {self.manufacturer} \n" \
               f"Model: {self.model} \n" \
               f"Fuel consumption: {self.fuel_consumption} \n" \
               f"Car year: {self.car_year}\n" \
               f"Price: {self.price}\n" \
               f"Max speed: {self.max_speed}\n"


list_of_models = ['ST65', 'Y78', 'ST300', 'X100', 'P480', 'BFG300', 'Kuga', 'Urus', 'T400', 'Focus']
list_of_manufacturers = ['Ford', 'Scania', 'Porche', 'Renault', 'Volvo']
list_of_fuel_consumption = [element + round(random.random(), 1) for element in range(10, 30)]
list_of_lifting_capacity = [element for element in range(1000, 30000, 1000)]
list_of_max_speed = [element for element in range(240, 400)]
list_of_price = [element for element in range(500000, 40000000, 50000)]
list_of_production_year = [element for element in range(1980, 2023)]

for elemen in range(50):
    cargo_car = CargoCar(
        fuel_consumption=random.choice(list_of_fuel_consumption),
        manufacturer=random.choice(list_of_manufacturers),
        model=random.choice(list_of_models),
        lifting_capacity=random.choice(list_of_lifting_capacity),
        car_year=random.choice(list_of_production_year)
    )
    del cargo_car
    sport_car = SportCar(
        fuel_consumption=random.choice(list_of_fuel_consumption),
        manufacturer=random.choice(list_of_manufacturers),
        model=random.choice(list_of_models),
        max_speed=random.choice(list_of_max_speed),
        price=random.choice(list_of_price),
        car_year=random.choice(list_of_production_year)
    )
    del sport_car
