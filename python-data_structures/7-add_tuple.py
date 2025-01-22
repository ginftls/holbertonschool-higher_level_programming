#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements by padding with zeros
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Only take the first two elements of each tuple
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Add the corresponding elements and return as a new tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
