def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Delete the item at the specified index in place
    del my_list[idx]
    # Return the modified list
    return my_list
