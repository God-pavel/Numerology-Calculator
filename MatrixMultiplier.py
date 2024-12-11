class MatrixMultiplier:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def compute_matrix_product(self):
        result = []
        if len(self.m1[1]) != len(self.m2) :
            raise Exception("Matrices cannot be multiplied, as the number of columns in matrix m1 does not equal the number of rows in matrix m2.")
        for i in range(len(self.m1)):
            result_row = []
            for g in range(len(self.m1)):
                result_row.append(self.__calculate_field(i, g))
            result.append(result_row)
        return result


    def __calculate_field(self, i, g):
        field = 0
        for l in range(len(self.m2)):
            field += self.m1[i][l] * self.m2[l][g]
        return field



    def matrix_to_string(self, matrix):
        return "\n".join(" ".join(f"{elem:5}" for elem in row) for row in matrix)