#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples with 0s if needed, and limit to first 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Return new tuple with sum of first two elements
    return (a[0] + b[0], a[1] + b[1])
