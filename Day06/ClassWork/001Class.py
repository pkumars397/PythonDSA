class Car:
    wheels=4 #class variable
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color 
    def show_details(self):
        print(f"This car is {self.color} {self.brand}")
    def __str__(self): #it will print str of a object
        return f"{self.color} {self.brand} with {self.wheels}" 
    
car1=Car("Toyota","Yellow")
car2=Car("Honda","Blue")
car1.show_details()
car2.show_details()
Car.wheels=5
car1.wheels=4
print(car1.wheels)
print(car2.wheels)

print(car1)
print(car2)