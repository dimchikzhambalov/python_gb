class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(''.join('%d\t' % j for j in i) for i in self.matrix)

    def __add__(self, other):
        try:
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    new_matrix = self.matrix
            return Matrix(new_matrix)
        except IndexError:
            print("Матрицы должны быть одинакового размера")


matrix_1 = Matrix([[32, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[11, 21], [32, 26], [75, 40]])

print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
