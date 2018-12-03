class Car:
    "Name of the class is car"
    totalNumber = 0
    def __init__(self, make, model, year):
        Car.totalNumber+=1
        self.make = make
        self.model = model
        self.year = year
        print("Instance of the object is created")

    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print()


car1 = Car("A", "B", 2018)
car2 = Car("C", "D", 2019)

print("Total number of car is: ",Car.totalNumber)