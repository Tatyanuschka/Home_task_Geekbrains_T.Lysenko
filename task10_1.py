class Matrix:

    def __init__(self, list):
        self.list = list


    def __str__(self):
        # res = ''
        # for i in range(len(self.list)):
        #     for j in range(len(self.list[i])):
        #         res += str(self.list[i][j]) + ' '
        #         if j == len(self.list[i]) - 1:
        #             res += '\n'
        # return res
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.list)

    def __add__(self, other):
        if not len(self.list) == len(other.list):
            raise ValueError('Разный размер у матриц')
        else:
            for i in range(len(self.list)):
                if not len(self.list[i]) == len(other.list[i]):
                    raise ValueError('Матрицы имеют разный размер')
            res = [[int(self.list[i][j]) + int(other.list[i][j]) for j in range(len(self.list[i]))]
                       for i in range(len(self.list))]
            # for j in range(len(self.list[i])):
            #     res_under.append(self.list[i][j] + other.list[i][j])
            # res.append(res_under)
        return Matrix(res)


a1 = Matrix([[31, 22], [37, 43], [51, 86]])
a2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
a3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
a4 = Matrix([[39, 184,0], [220,-15,4], [100, 34, 8]])
print(a1)
print(a2)
print(a3)
a_add = a2 + a4
print(a_add)
