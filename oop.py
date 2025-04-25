class vehicle:
 def __init__(self, color, brand, engine_capacity, year):
        self.color = color
        self.brand = brand
        self.engine_capacity = engine_capacity
        self.year = year
def __str__(self):
        return f"Vehicle(color={self.color}, brand={self.brand}, engine_capacity={self.engine_capacity}, year={self.year})"
vehicle1 = vehicle('grey', 'toyota', '1800', '2020')
vehicle2 = vehicle('black', 'honda', '2000', '2021')
vehicle3 = vehicle('blue', 'ford', '2500', '2022')
vehicle4 = vehicle('red', 'chevrolet', '3000', '2023')
vehicle5 = vehicle('white', 'nissan', '3500', '2024')
vehicle6 = vehicle('yellow', 'subaru', '4000', '2025')
class car(vehicle):
    pass
    def move(self ):
        print(f"The {self.color} {self.brand} is driving.")
car1=car('grey','mitsubishi','1800','2020') 
car2=car('black','ford','2000','2021')
car3=car('blue','mercedes','2500','2022')
car4=car('red','audi','3000','2023')
car5=car('white','tesla','3500','2024')
car6=car('yellow','volvo','4000','2025')
car7=car('green','fiat','4500','2026')
car8=car('purple','chevrolet','5000','2027')
car9=car('pink','subaru','5500','2028')
car10=car('orange','honda','6000','2029')
class plane(vehicle):
    pass
    def move(self ):
     print(f"The {self.color} {self.brand} is flying.")
plane1=plane('grey','boeing','1800','2020')
plane2=plane('black','airbus','2000','2021') 
plane3=plane('blue','lockheed','2500','2022')
plane4=plane('red','bombardier','3000','2023')
plane5=plane('white','embraer','3500','2024')
plane6=plane('yellow','cessna','4000','2025')
class boat(vehicle):
    pass
    def move(self ):
     print(f"The {self.color} {self.brand} is sailing.")
boat1=boat('grey','yacht','1800','2020')
boat2=boat('black','fishing boat','2000','2021') 
boat3=boat('blue','cargo ship','2500','2022')
boat4=boat('red','sailboat','3000','2023')
boat5=boat('white','speedboat','3500','2024')
boat6=boat('yellow','tugboat','4000','2025')
car1.move()
plane1.move()
boat5.move()
print(car1.brand)

