#!/usr/bin/python3
import pickle


class CustomObject:
    """
    A custom class with attributes for serialization
    and deserialization using pickle.
    """
    def __init__(self, name, age, is_student):
        """Initialize the object with name, age, and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file
        and returns an instance of CustomObject."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
