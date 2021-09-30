class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(map(str, self.data))

    def __add__(self, other):
        lst = []
        for i in range(len(self.data)):
            lst.append([])
            for j in range(len(self.data[0])):
                lst[i].append(self.data[i][j] + other.data[i][j])
        return Matrix(lst)


mtx1 = Matrix([[1, 3, 5], [2, 4, 6], [3, 5, 7]])
mtx2 = Matrix([[4, 6, 8], [5, 7, 9], [6, 8, 0]])
print(f'matrix 1:\n{mtx1}')
print(f'matrix 2:\n{mtx2}')
print(f'matrix 1 + matrix 2:\n{mtx1 + mtx2}')
