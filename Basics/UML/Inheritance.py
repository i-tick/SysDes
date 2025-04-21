# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating...")

# Child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...")

# Using the child class
if __name__ == "__main__":
    my_dog = Dog("Buddy")
    my_dog.eat()  # Inherited from Animal class
    my_dog.bark()  # Defined in Dog class