#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store True or False for each element
    result_list = []
    # Iterate through the original list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    # Return the new list
    return result_list
