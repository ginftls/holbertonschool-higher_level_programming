#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    :param data: Dictionary to serialize
    :param filename: Name of the JSON file to save the data
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file into a Python dictionary.

    :param filename: Name of the JSON file to load the data from
    :return: Deserialized Python dictionary
    """
    with open(filename, 'r') as file:
        return json.load(file)
