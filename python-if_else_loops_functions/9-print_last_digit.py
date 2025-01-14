#!/usr/bin/python3
def print_last_digit(number):
    # Handle negative numbers by taking the absolute value
    last_digit = abs(number) % 10
    # Print the last digit without a newline
    print(last_digit, end="")
    # Return the last digit
    return last_digit
