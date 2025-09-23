class cars:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info (self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}") 

c1 = cars ("Toyota","Innova Crysta", 2021)
c2 = cars ("Suzuki", "Swift", 2024)
c3 = cars ("Audi", "Q7", 2010)
c1.car_info() 
c2.car_info()  
c3.car_info()  

