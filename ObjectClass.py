class Car:
    "Name of the class is car"
    def __init__ (self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        print("Instance of the object is created")


    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)  
        print("Year: ", self.year)
        print()

car1 =Car("A","B",2018) 
car1.displayParameters()       