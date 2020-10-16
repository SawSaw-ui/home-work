class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        m = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

        for i in range(len(self.list_1)):

            for x in range(len(self.list_2[i])):
                m[i][x] = self.list_1[i][x] + self.list_2[i][x]

        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in m]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in m]))


my_matrix = Matrix([[2, 3, 4],
                    [5, 6, 7],
                    [8, 9, 10]],
                   [[11, 12, 13],
                    [14, 15, 16],
                    [17, 18, 19]])

print(my_matrix.__add__())
