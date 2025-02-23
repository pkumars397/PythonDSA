#Animal class ,name,species,make_sound
#cat ,dog
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species 
    def make_sound(self):
        print("Some generic sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog=Dog("Buddy","DOg")
cat=Cat("Whiskers","Cat")
print(dog.name)
dog.make_sound()
cat.make_sound()