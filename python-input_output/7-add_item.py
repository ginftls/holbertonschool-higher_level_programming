#!/usr/bin/python3


"""
Script that adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os
from json import dump as save_to_json_file
from json import load as load_from_json_file

FILENAME = "add_item.json"

# Check if the file exists and load its content,
# otherwise start with an empty list
if os.path.exists(FILENAME):
    my_list = load_from_json_file(FILENAME)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save updated list back to the file
save_to_json_file(my_list, FILENAME)
