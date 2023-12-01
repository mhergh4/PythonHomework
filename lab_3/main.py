import numpy as np

def multiply_vector_matrix(vector, matrix):
    result = np.dot(vector, matrix)
    return result

def write_result_to_file(result, filename):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":

    vector = np.array([1, 2, 3])

    matrix = np.array([[4, 5, 6],
                       [7, 8, 9],
                       [10, 11, 12]])

    result = multiply_vector_matrix(vector, matrix)

    filename = "result.txt"
    write_result_to_file(result, filename)

    print("Result array:")
    print(result)
    print(f"Result has been written to {filename}.")
