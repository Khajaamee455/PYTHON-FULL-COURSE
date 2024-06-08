# Inheritance in python 
# Inheritanc is nothing but whenever we construct a new class from an existing class 
# that new class can access the properties and behaviours of existing class is called as 
# inheritance....


class Animal :
    def __init__(self , name , legs ) :
        self.name = name 
        self.legs = legs
        
class Dog(Animal):
    def sound(self):
        print("bow bow ")
        
        
tommy = Dog("tommy" ,4)
print(tommy.name)
print(tommy.legs)
tommy.sound()