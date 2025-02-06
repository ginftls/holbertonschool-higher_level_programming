#!/usr/bin/env python3
from abc import ABC, abstractmethod


# Define the abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method, must be implemented in subclasses


# Define the Dog subclass
class Dog(Animal):
    def sound(self):
        return "Bark"


# Define the Cat subclass
class Cat(Animal):
    def sound(self):
        return "Meow"


if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())  # Output: Bark
    print(garfield.sound())  # Output: Meow

    # Attempting to instantiate Animal will raise an error
    # animal = Animal()  # Uncommenting this will result in TypeError
