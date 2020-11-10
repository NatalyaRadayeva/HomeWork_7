# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()

class Matrix(object):
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for a in range(len(self.list_1)):

            for b in range(len(self.list_2[a])):
                matr[a][b] = self.list_1[a][b] + self.list_2[a][b]

        return str('\n'.join(['\t'.join([str(b) for b in a]) for a in matr]))


def __str__(self):
    return str('\n'.join(['\t'.join([str(b) for j in a]) for a in matr]))


my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[11, 12, 13],
                    [14, 15, 16],
                    [17, 18, 19]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())
