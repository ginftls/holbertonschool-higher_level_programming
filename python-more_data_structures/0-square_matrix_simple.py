#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = []
     # Iterate over each row in the matrix
    for row in matrix:
        # Create a new row to store the squared values
        new_row = []
         # Iterate over each element in the row
        for element in row:
            # Square the element and append it to the new row
            new_row.append(element ** 2)
        # Append the new row to the new matrix
        new_matrix.append(new_row)
    # Return the new matrix
    return new_matrix
