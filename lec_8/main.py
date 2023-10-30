class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total = sum(sum(row) for row in self.matrix)
        return total / (self.n * self.m)

    def calculate_row_sum(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            return None

    def calculate_column_average(self, column_index):
        if 0 <= column_index < self.m:
            total = sum(row[column_index] for row in self.matrix)
            return total / self.n
        else:
            return None

    def print_submatrix(self, indices):
        col1, col2, row1, row2 = indices
        if 0 <= col1 < col2 <= self.m and 0 <= row1 < row2 <= self.n:
            submatrix = [row[col1:col2] for row in self.matrix[row1:row2]]
            for row in submatrix:
                print(row)
        else:
            print("Invalid submatrix indices.")

n = 4
m = 3
matrix = Matrix(n, m)

matrix.matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print("Matrix:")
matrix.print_matrix()

mean = matrix.calculate_mean()
print(f"Mean of the matrix: {mean}")

row_sum = matrix.calculate_row_sum(2)  
if row_sum is not None:
    print(f"Sum of row 2: {row_sum}")
else:
    print("Invalid row index.")

col_average = matrix.calculate_column_average(1)  
if col_average is not None:
    print(f"Average of column 1: {col_average}")
else:
    print("Invalid column index.")

print("Submatrix:")
matrix.print_submatrix([1, 3, 0, 2])  
