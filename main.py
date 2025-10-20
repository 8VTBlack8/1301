import random

def generate_matrix(rows, cols):
    # генереция чисел от -100 до 100
    return [[random.randint(-100,100) for _ in range(cols)]for _ in range(rows)]

def add_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range (rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    rows, cols = 10, 10
    matrix_1 = generate_matrix(rows,cols)
    matrix_2 = generate_matrix(rows,cols)

    print("Матрица 1: ")
    print_matrix(matrix_1)

    print("Матрица 2: ")
    print_matrix(matrix_2)

    matrix_3 = add_matrix(matrix_1,matrix_2)
    print("\nРезультат сложения матриц (Матрица 3): ")
    print_matrix(matrix_3)