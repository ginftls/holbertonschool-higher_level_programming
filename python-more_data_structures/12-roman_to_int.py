#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral string to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Roman numeral values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate over the Roman numeral string in reverse order
    for char in reversed(roman_string):
        value = roman_values.get(char, 0)
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value

    return total
