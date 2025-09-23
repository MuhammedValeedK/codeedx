class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Car (vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type      

    def show_info(self):
        super().show_info()
        print(f"Fuel Type: {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, "Electric")
        self.battery_capacity = battery_capacity

    def show_info(self):
        super().show_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


my_car1 = ElectricCar("Tesla", "Model S", 75)
my_car1.show_info()


