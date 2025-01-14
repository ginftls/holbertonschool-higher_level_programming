#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 from its ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
