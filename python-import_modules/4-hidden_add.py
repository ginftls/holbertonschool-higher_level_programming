#!/usr/bin/env python3

import hidden_4

if __name__ == "__main__":
    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter out names that start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort the names alphabetically
    sorted_names = sorted(filtered_names)

    # Print one name per line
    for name in sorted_names:
        print(name)
