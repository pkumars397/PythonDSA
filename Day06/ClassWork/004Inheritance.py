#We have parent class whose properties and behaviours we can use in child class
class Vehicle:
    #init is used to intialise the variables of the class instances and it is constructor
    #it is inbuilt method and its called automatically when object created
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def show_details(self):
        print(f"this is {self.color} {self.brand}")
class Car(Vehicle):
    def __init__(self,brand,color,doors):
        #super is used to call parent class methods
        #here we are intializing brand and color using parent constructor
        super().__init__(brand,color)
        self.door=doors
    def show_details(self):
        print(f"this is {self.color} {self.brand} has {self.door}")

class Electric:
    def __init__(self,battery_capacity):
        self.battery_capacity=battery_capacity
    def battery_info(self):
        print(f"this is vehicle has a {self.battery_capacity} kmh battery.")

#child class
class ElectricCar(Vehicle,Electric):
    def __init__(self,brand,color,battery_capacity):
        Vehicle.__init__(self,brand,color)
        Electric.__init__(self,battery_capacity)

class Bike(Vehicle):
    def __init__(self,brand,color,engine_cc):
        super().__init__(brand,color)
        self.engine_cc=engine_cc

    def show_details(self):
        print(f"this {self.color} {self.brand} with {self.engine_cc} cc engine")

tesla=ElectricCar("Tesla","White",75)
tesla.show_details()
tesla.battery_info()

car1=Car("Toyoto","red",4)
car1.show_details()
v1=Vehicle("Maruti","white")
v1.show_details()
bike1=Bike("Yamaha","Blue",150)
bike1.show_details()