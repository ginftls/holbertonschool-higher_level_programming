#!/usr/bin/python3
def multiple_returns(sentence):
    # Calculate the length of the sentence
    length = len(sentence)
     # Determine the first character
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
     # Return a tuple with the length and the first character
    return (length, first_char)
