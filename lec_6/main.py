import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    if column_index < 0 or column_index >= len(matrix[0]):
        return None  
    column_sum = 0
    for row in matrix:
        column_sum += row[column_index]
    return column_sum

def get_row_average(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        return None  
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average

rows = 4
cols = 3
matrix = generate_random_matrix(rows, cols)
print("Generated Matrix:")
for row in matrix:
    print(row)

column_index = 1
column_sum = get_column_sum(matrix, column_index)
if column_sum is not None:
    print(f"Sum of column {column_index}: {column_sum}")
else:
    print(f"Invalid column index: {column_index}")

row_index = 2
row_average = get_row_average(matrix, row_index)
if row_average is not None:
    print(f"Average of row {row_index}: {row_average}")
else:
    print(f"Invalid row index: {row_index}")
