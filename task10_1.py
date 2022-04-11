class Matrix:

    def __init__(self, list, start=0):
        self.list = list
        self.i = start
        self.start = start

    def __str__(self):
        res = ''
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                res += str(self.list[i][j]) + ' '
                if j == len(self.list[i]) - 1:
                    res += '\n'
        return res

    def __add__(self, other):
        res = []
        for i in range(len(self.list)):
            res_under = []
            for j in range(len(self.list[i])):
                res_under.append(self.list[i][j] + other.list[i][j])
            res.append(res_under)
        return res


a1 = Matrix([[31, 22], [37, 43], [51, 86]])
a2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
a3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
a4 = Matrix([[39, 184,0], [220,-15,4], [100, 34, 8]])
print(a1)
print(a2)
print(a3)
a_add = Matrix(a2 + a4)
print(a_add)
