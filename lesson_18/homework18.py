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

    def __str__(self):
        return f"Manufacturer: {self.manufacturer} \n" \
               f"Model: {self.model} \n" \
               f"Fuel consumption: {self.fuel_consumption} \n" \
               f"Car year: {self.car_year}"


car1 = Car(fuel_consumption=8.0, manufacturer='Ford', model='Kuga', car_year=2013)
car2 = Car(fuel_consumption=5.6, manufacturer='Toyota', model='Supra', car_year=2018)
car3 = Car(fuel_consumption=7.65, manufacturer='Porche', model='911', car_year=2010)

print(car1, end='\n\n')
print(car2, end='\n\n')
print(car3)
