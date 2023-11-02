class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            if len(data) == rows and all(len(row) == cols for row in data):
                self.data = data
            else:
                raise ValueError("Invalid data dimensions for the matrix.")
        else:
            self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.data)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")
        result = []
        for i in range(self.rows):
            result_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            result.append(result_row)
        return Matrix(self.rows, self.cols, result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")
        result = []
        for i in range(self.rows):
            result_row = [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            result.append(result_row)
        return Matrix(self.rows, self.cols, result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")
        result = []
        for i in range(self.rows):
            result_row = []
            for j in range(other.cols):
                dot_product = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                result_row.append(dot_product)
            result.append(result_row)
        return Matrix(self.rows, other.cols, result)

matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(2, 3, [[7, 8, 5], [9, 10, 4]])

result_addition = matrix1 + matrix2
print("Addition result:")
print(result_addition)

result_subtraction = matrix1 - matrix2
print("\nSubtraction result:")
print(result_subtraction)

result_multiplication = matrix1 * matrix2
print("\nMultiplication result:")
print(result_multiplication)
