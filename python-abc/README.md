# Python - Abstract Classes and Interfaces

## Introduction
This document provides an overview of abstract classes and interfaces in Python. Abstract classes and interfaces are essential concepts in object-oriented programming that help in defining and enforcing a contract for subclasses.

## Abstract Classes
An abstract class is a class that cannot be instantiated and is typically used as a base class. Abstract classes can contain abstract methods, which are methods declared but contain no implementation. Subclasses of an abstract class are required to implement the abstract methods.

### Example
```python
from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    return "Bark"

class Cat(Animal):
  def make_sound(self):
    return "Meow"
```

## Interfaces
In Python, interfaces can be implemented using abstract base classes (ABCs). An interface is a collection of abstract methods that a class must implement. Interfaces help in defining a contract that the implementing classes must follow.

### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)
```

## Conclusion
Abstract classes and interfaces are powerful tools in Python that help in designing robust and maintainable code. They provide a way to define a common interface for a group of related classes and enforce a contract for subclasses to implement specific methods.
